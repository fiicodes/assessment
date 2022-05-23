



from django.urls import path,include
from django import urls
from apiapp import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from  rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView


urlpatterns = [
   
    path('login/',views.CustomAuthTokenlogin.as_view()),#To authenticate user for creating todo tasks.
   
    path('todocontroller/', views.TodoList.as_view()),#Endpoint to  view the list of task
    path('todocontroller/<int:pk>/', views.TodoDetail.as_view()),#Endpoint to perform delete,update,retrive the task
    path('AuthController/', CustomTokenObtainPairView.as_view(), name='AuthController'),#Endpoint to authenticate the Authcontroller with jwt
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

]


urlpatterns = format_suffix_patterns(urlpatterns)









  