from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):

	class UserTypeChoices(models.TextChoices):
		SUPERUSER = 'superuser'
		USER = 'user'

	user_type = models.CharField(choices=UserTypeChoices.choices,max_length=20)
	phone_regex = RegexValidator(
        regex=r"(0/91)?[6-9][0-9]{9}",
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.",
    )
	phone = models.CharField(validators=[phone_regex],max_length=30,unique=True,null=True)
	profile_image = models.ImageField(upload_to='profile_images',null=True,blank=True)
	user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Use a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
	groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Use a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
	# username
	# first_name
	# last_name
	# email
	# is_active
	# date_joined

	def __str__(self):
		return self.username
