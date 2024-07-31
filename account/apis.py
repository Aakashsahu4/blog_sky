"""External Imports"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

"""Internal Imports"""
from account import models as account_models
from account import serializers as account_serializers
from master import utils as master_utils

class CreateUserAPI(APIView):
	"""API to create a user"""
	def post(self, request):
		serializer = account_serializers.UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return master_utils.custom_response(serializer.data, status=status.HTTP_201_CREATED)
		return master_utils.custom_response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetUserAPI(APIView):
	"""API to retrieve a user data"""
	def get(self, request):
		user_id = request.user.id
		if user_id:
			try:
				user = account_models.User.objects.get(id=user_id)
				serializer = account_serializers.UserSerializer(user,context={'request':request})
				return Response(serializer.data)
			except account_models.User.DoesNotExist:
				return master_utils.custom_response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
		# user = account_models.User.objects.all()
		# serializer = account_serializers.UserSerializer(user,many=True,context={'request':request})
		return Response('No User Found')

class UpdateUserAPI(APIView):
	"""API to update a user data"""
	def patch(self, request, user_id):
		try:
			user = account_models.User.objects.get(id=user_id)
			serializer = account_serializers.UserSerializer(user, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return master_utils.custom_response(serializer.data, status=status.HTTP_200_OK)
			return master_utils.custom_response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except account_models.User.DoesNotExist:
			return master_utils.custom_response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class DeleteUserAPI(APIView):
	"""API to delete a user data"""
	def post(self, request, user_id):
		try:
			user = account_models.User.objects.filter(id=user_id)
			user.update(is_active=False)
			return master_utils.custom_response({"message": "User deleted"}, status=status.HTTP_200_OK)
		except account_models.User.DoesNotExist:
			return master_utils.custom_response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)



class LoginUser(APIView):
	"""API to login a user"""
	def post(self, request):
		try:
			username = request.data.get('username')
			password = request.data.get('password')
			user = account_models.User.objects.get(username=username)
			if user.password == password:
				token = master_utils.get_tokens_for_user(user)
				return master_utils.custom_response({"token": token}, status=status.HTTP_200_OK)
			else:
				return master_utils.custom_response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
		except account_models.User.DoesNotExist:
			return master_utils.custom_response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class WebSocket(APIView):

	def get(self,request):
		return Response({'message':'Hiiiii Sagar'})