from django.contrib import admin
from database.models import User, Rating

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','id')
admin.site.register(User,UserAdmin)
admin.site.register(Rating)
