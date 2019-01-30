from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from Dummy.serializers import *
from Dummy.models import *

from itertools import chain


# Create your views here.
class UserView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class OBFCreateView(generics.CreateAPIView):
	serializer_class = OBFSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class OBFUpdateView(generics.UpdateAPIView):
	serializer_class = OBFSerializer
	permission_classes = (IsAuthenticated, )

	def perform_update(self, serializer):
		if serializer.owner == self.request.user:
			instance = serializer.save()

class OBFListView(generics.ListAPIView):
	serializer_class = OBFSerializer
	# permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		if (user.is_anonymous) :
			obfs = OBF.objects.all()
		else:
			obfs = list(chain(OBF.objects.filter(owner=user), OBF.objects.filter(isPrivate=False)))
		return obfs


class OBZCreateView(generics.CreateAPIView):
	serializer_class = OBZSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class OBZUpdateView(generics.UpdateAPIView):
	serializer_class = OBZSerializer
	permission_classes = (IsAuthenticated, )

	def perform_update(self, serializer):
		if serializer.owner == self.request.user:
			instance = serializer.save()

class OBZListView(generics.ListAPIView):
	serializer_class = OBZSerializer
	# permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		obfz = list(chain(OBZ.objects.filter(owner=user), OBZ.objects.filter(isPrivate=False)))
		return obfz


class SymbolCreateView(generics.CreateAPIView):
	serializer_class = SymbolSerializer
	# permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		if (self.request.user.is_anonymous) :
			serializer.save(owner=None)
		else: 
			serializer.save(owner=self.request.user)

class SymbolListView(generics.ListAPIView):
	serializer_class = SymbolSerializer
	# permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		if (user.is_anonymous) :
			symbols = Symbol.objects.all()
		else :
			symbols = list(chain(Symbol.objects.filter(owner=user), Symbol.objects.filter(isPrivate=False)))

		return symbols
		