from django.urls import path
from . import views

urlpatterns = [
    path(
        route='posts/new',
        view=views.CreatePostView.as_view(),
        name='create'
    ),
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),
    path(
        route='posts/detail/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),

]
