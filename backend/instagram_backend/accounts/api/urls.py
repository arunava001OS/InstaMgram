from django.urls import path

from accounts.api import views

urlpatterns = [
    path('register/',views.register_view,name="register"),
    path('login/',views.login_view,name="register"),
    path('update_profile/',views.profile_update_view,name="register"),
]
