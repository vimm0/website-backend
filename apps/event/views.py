from django.views.generic import DetailView

from apps.event.models import Event
from hotc.utils.views import ListView


class EventsList(ListView):
    queryset = Event.objects.filter(enabled=True).order_by('-start')
    search_fields = ['title', 'start']
    search_exact_fields = []


class EventDetail(DetailView):
    queryset = Event.objects.filter(enabled=True)
