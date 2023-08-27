from django.contrib import admin
from .models import UserProfile, CastomUser

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(CastomUser)
