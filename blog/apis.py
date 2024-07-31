"""External Imports"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

"""Internal Imports"""
from . import models as blog_models
from . import serializers as blog_serializers
from master import utils as master_utils
from account import models as account_models

class CreateBlogAPI(APIView):
	permission_classes = [permissions.IsAuthenticated]
	"""API to create a blog"""
	def post(self, request):
		serializer = blog_serializers.BlogSerializer(data=request.data)
		if serializer.is_valid():
			user = account_models.User.objects.get(id=request.user.id)
			serializer.save(user_profile=user)
			return master_utils.custom_response(serializer.data, status=status.HTTP_201_CREATED)
		return master_utils.custom_response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetBlogAPI(APIView):
	"""API to retrieve a blog data"""
	def get(self, request):
		blog_id = request.GET.get('blog',None)
		if blog_id:
			try:
				blog = blog_models.Blog.objects.get(id=blog_id)
				serializer = blog_serializers.GetBlogSerializer(blog,context={'request':request})
				return Response(serializer.data)
			except blog_models.Blog.DoesNotExist:
				return master_utils.custom_response({"error": "Blog Doesn't exists anymore"}, status=status.HTTP_404_NOT_FOUND)
		blog = blog_models.Blog.objects.all().order_by('-created')
		serializer = blog_serializers.GetBlogSerializer(blog,many=True,context={'request':request})
		return master_utils.custom_response(serializer.data,status=status.HTTP_200_OK)

class UpdateBlogAPI(APIView):
	"""API to update a blog data"""
	def patch(self, request, blog):
		try:
			blog = blog_models.Blog.objects.get(id=blog)
			serializer = blog_serializers.BlogSerializer(blog, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return master_utils.custom_response(serializer.data, status=status.HTTP_200_OK)
			return master_utils.custom_response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except blog_models.Blog.DoesNotExist:
			return master_utils.custom_response({"error": "Invalid Blog"}, status=status.HTTP_404_NOT_FOUND)


class DeleteBlogAPI(APIView):
	"""API to delete a blog data"""
	def delete(self, request, blog):
		try:
			blog = blog_models.Blog.objects.get(id=blog)
			blog.delete()
			return master_utils.custom_response({"message": "Blog deleted successfully"}, status=status.HTTP_200_OK)
		except blog_models.Blog.DoesNotExist:
			return master_utils.custom_response({"error": "Blog no longer exists"}, status=status.HTTP_404_NOT_FOUND)


class GetNotificationsListAPI(APIView):
	"""API to retrieve a blog data"""
	def get(self, request):
		notification_id = request.GET.get('id',None)
		if notification_id:
			try:
				notification = blog_models.Notification.objects.get(id=notification_id)
				serializer = blog_serializers.NotificationSerializer(notification,context={'request':request})
				return Response(serializer.data)
			except blog_models.Notification.DoesNotExist:
				return master_utils.custom_response({"error": "Object Doesn't exists"}, status=status.HTTP_404_NOT_FOUND)
		notification = blog_models.Notification.objects.all().order_by('-created')
		serializer = blog_serializers.NotificationSerializer(notification,many=True,context={'request':request})
		return master_utils.custom_response(serializer.data,status=status.HTTP_200_OK)