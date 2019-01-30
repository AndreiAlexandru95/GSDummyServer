from Dummy.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class OBZSerializer(serializers.ModelSerializer):
	class Meta:
		model = OBZ
		fields = ('owner_id', 'obz_content', 'isPrivate')


class SymbolSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symbol
		fields = ('owner_id', 'name', 'locale', 'license', 'author', 'author_url', 'source_url', 'extension', 'image_url', 'isPrivate')


class OBFSerializer(serializers.ModelSerializer):
	class Meta:
		model = OBF
		fields = ('owner_id', 'obf_content', 'isPrivate')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
		return user