from django.contrib import admin
from users.models import Profile
from posts.models import Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
