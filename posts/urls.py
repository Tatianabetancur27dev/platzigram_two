from django.urls import path
from . import views


urlpatterns = [

    path(
        route='feed/',
        view=views.list_posts,
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.create_post,
        name='create'
    ),
]
