from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User

admin.site.unregister(User)
admin.site.unregister(Group)
