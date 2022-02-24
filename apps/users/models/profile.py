from django.db import models

from apps.utils.models import BaseModel


class Profile(BaseModel):
    SEXES = (
        ('M', u'Male'),
        ('F', u'Female'),
    )
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    avatar = models.ImageField('profile avatar', upload_to='users/avatar', blank=True, null=True)
    biography = models.TextField(max_length=360, blank=True)
    address = models.Charfiels('address users', max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEXES, default="M")

    def __str__(self) -> str:
        return str(self.user)
