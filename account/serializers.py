from rest_framework import serializers
from account import models as account_model


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = account_model.User
		fields = ('__all__')