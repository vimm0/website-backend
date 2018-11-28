from django import forms
from django_summernote.widgets import SummernoteWidget

from apps.event.models import Event


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'description_pre': SummernoteWidget(),
            'description_post': SummernoteWidget(),
            'description_common': SummernoteWidget(),
        }
