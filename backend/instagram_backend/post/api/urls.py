from django.urls import path
from . import views

urlpatterns = [
    # path('create_post/',views.create_post,name="create-post"),
    # path('view_post/<int:pk>/',views.view_post,name="view-post"),
    # path('delete_post/<int:pk>/',views.delete_post,name="view-post"),

    # path('view_post/<str:username>/',views.view_posts_username,name="view-postlist"),
    path('posts/',views.PostListView.as_view(),name='list all posts'),
    path('posts/<int:pk>/',views.PostDetailView.as_view(),name='detail-post'),
]