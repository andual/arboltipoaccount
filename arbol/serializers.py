from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Account
		fields = ('number', 'name', 'Type', 'parent','owner' )

class UserSerializer(serializers.ModelSerializer):
	accounts = serializers.PrimaryKeyRelatedField(
		many=True, queryset=Account.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username', 'accounts')