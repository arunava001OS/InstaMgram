from django.urls import path
from . import views

urlpatterns = [
    path('follow/',views.FollowshipView.as_view(),name='follow'),
]