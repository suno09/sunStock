from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Rank(models.IntegerChoices):
    MASTER = 0, "DEVELOPER"
    ADMIN = 1, "ADMIN"
    OTHER = 2, "OTHER"


class UserInfo(models.Model):
    # user is foreign key
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    rank = models.IntegerField(choices=Rank.choices,
                               default=Rank.OTHER)
    # image = models.ImageField(upload_to='user_images', blank=True)

    def __str__(self):
        return f'UserInfo{{user="{self.user.username}", ' \
               f'rank="{self.rank}"}}'
