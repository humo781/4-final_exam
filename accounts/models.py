from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    profile_image = models.ImageField(
        upload_to='profile_images/',
        default='profile_images/default.jpg',
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=False, null=False, unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions'
    )

    def __str__(self):
        return self.username
