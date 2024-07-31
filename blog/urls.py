from django.urls import include,path
from . import apis

urlpatterns = [
	path('create-blog/',apis.CreateBlogAPI.as_view()),
	path('get-blog/',apis.GetBlogAPI.as_view()),
	path('update-blog/<int:blog>/',apis.UpdateBlogAPI.as_view()),
	path('delete-blog/<int:blog>/',apis.DeleteBlogAPI.as_view()),
	path('get-notification/',apis.GetNotificationsListAPI.as_view()),
]