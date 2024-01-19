from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Notice, Community, Adboard, Taxi, ClubApplication

class ClubApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'club_name']

# Register your models here.
admin.site.register(Notice)
admin.site.register(Community)
admin.site.register(Adboard)
admin.site.register(Taxi)
admin.site.register(ClubApplication, ClubApplicationAdmin)
admin.site.register(User, UserAdmin)

UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname", "department")}),)