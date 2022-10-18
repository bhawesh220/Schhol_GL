from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_number', 'IGL_Username', 'email',  'profile_image',
                   'index_points', 'referral_code',)


admin.site.register(User, UserAdmin)
