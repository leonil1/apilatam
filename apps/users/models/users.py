from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from apps.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    email = models.EmailField('email addess', unique=True,
                              error_messages={'uniqui': 'A user with that email already exists.'})
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$', message='phone number enter of format +519999999')
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField('client status', default=True, help_text='is client user of store')
    is_admin = models.BooleanField('admin status', default=False, help_text='is admin of store enter all aplication')
    is_verified = models.BooleanField('verified status client', default=False,
                                      help_text='es verified have its email address')

    def __str__(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username
