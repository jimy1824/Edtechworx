from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import HomeBanner
from courses.models import Course
from event.models import Events
from blog.models import Blogs
# from .forms import MyForm

class Home(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        homebanner=HomeBanner.objects.filter().last()
        courses=Course.objects.filter().all()
        events=Events.objects.filter().all()
        blogs=Blogs.objects.filter().all()
        return render(request, self.template_name, {'homebanner': homebanner,'courses':courses,'events':events,'blogs':blogs})
        # return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})