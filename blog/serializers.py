from rest_framework import serializers
from . import models as blog_models
from account import serializers as account_serializers


class BlogSerializer(serializers.ModelSerializer):

	class Meta:
		model = blog_models.Blog
		fields = ('title','content')

class GetBlogSerializer(serializers.ModelSerializer):
	user_profile = account_serializers.UserSerializer()

	class Meta:
		model = blog_models.Blog
		fields = ('__all__')

class NotificationSerializer(serializers.ModelSerializer):
	from_user = account_serializers.UserSerializer()
	to_user = account_serializers.UserSerializer()

	class Meta:
		model = blog_models.Notification
		fields = ('__all__')