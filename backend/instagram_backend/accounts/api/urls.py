from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token 

from . import views

urlpatterns = [
    path('register/',views.register_view,name="register"),
    path('login/',obtain_auth_token,name="login"),
    path('update_profile/',views.profile_update_view,name="profile-update"),
]
