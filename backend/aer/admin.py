from django.contrib import admin
from .models import TextFile, Image, Video, Email

# Register your models here.

admin.site.register(Video)
admin.site.register(Image)
admin.site.register(TextFile)
admin.site.register(Email)