from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from apps.users.models import User, Profile
from apps.users.serializers.profile_serializers import ProfileModelSerializer
from django.utils import timezone

import jwt
from datetime import timedelta


class UserModelSerializer(serializers.ModelSerializer):

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'profile')


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account in not active yet :(')
        self.context['user'] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignupSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=3, max_length=20,
                                     validators=[UniqueValidator(queryset=User.objects.all())]
                                     )
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$', message='phone number enter of format +519999999')
    phone = serializers.CharField(validators=[phone_regex], required=False)
    password = serializers.CharField(min_length=6, max_length=64)
    password_confirmation = serializers.CharField(min_length=6, max_length=64)
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError('Password  does not match.')
        password_validation.validate_password(password)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False, is_client=True)
        Profile.objects.create(user=user)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        verification_token = self.gen_verification_token(user)
        subject = 'Welcome @{}: Verify your account to start using store online'.format(user.username)
        from_email = 'Store shop <noreply@storeshop.com'
        content = render_to_string('email/users/account_verification.html',
                                   {'token': verification_token, 'user': user}
                                   )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()

    def gen_verification_token(self, user):
        expire_date = timezone.now() + timedelta(days=2)
        payload = {
            'user': user.username,
            'exp': int(expire_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token


class AccountVerificationSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, data):
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid Token')
        self.context['payload'] = payload
        return data

    def save(self):
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
