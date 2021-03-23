from django.urls import path,include

from .views import *

urlpatterns = [
    path('register/',views.register_view,anme="register"),
    path('login/',views.login_view,anme="register"),
    path('update_profile/',views.profile_update_view,name="register"),
]
