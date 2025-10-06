from django.contrib import admin
from .models import Post

admin.site.register(Post)  # allows post management in admin panel
