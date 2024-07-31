from django.urls import include,path
from account import apis
from account import views as account_views

urlpatterns = [
	path('index/', account_views.IndexView.as_view(), name='index'),
	path('create-user/',apis.CreateUserAPI.as_view()),
	path('get-user/',apis.GetUserAPI.as_view()),
	path('update-user/<int:user_id>/',apis.UpdateUserAPI.as_view()),
	path('delete-user/<int:user_id>/',apis.DeleteUserAPI.as_view()),
	path('login/',apis.LoginUser.as_view()),
	path('ws/',apis.WebSocket.as_view()),
]