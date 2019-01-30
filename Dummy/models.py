from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)


class OBF(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	obf_content = models.TextField()
	isPrivate = models.BooleanField(default=False)


class OBZ(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	obz_content = models.TextField()
	isPrivate = models.BooleanField(default=False)


class Symbol(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.TextField(null=True, blank=True)
	locale = models.TextField(null=True, blank=True)
	license = models.TextField(null=True, blank=True)
	author = models.TextField(null=True, blank=True)
	author_url = models.TextField(null=True, blank=True)
	source_url = models.TextField(null=True, blank=True)
	extension = models.TextField(null=True, blank=True)
	image_url = models.TextField(null=True, blank=True)
	isPrivate = models.BooleanField(default=False)