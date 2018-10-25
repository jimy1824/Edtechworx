from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Events
# from .forms import MyForm

class EventsList(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'events.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        events=Events.objects.filter().all()
        return render(request, self.template_name, {'events': events})
        # return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


class EventDetail(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'event-details.html'

    def get(self, request, event_id=None):
        # form = self.form_class(initial=self.initial)
        event_details = Events.objects.filter(id=event_id).first()
        return render(request, self.template_name, {'event_details': event_details})
        # return render(request, self.template_name)