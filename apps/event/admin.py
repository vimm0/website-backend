from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin

from apps.event.forms import EventModelForm
from .models import Event


class EventAdmin(admin.ModelAdmin):
    form = EventModelForm


admin.site.register(Event, EventAdmin)
