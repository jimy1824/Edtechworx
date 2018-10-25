from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Team,CompanyAbouts
# from .forms import MyForm

class About(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        team_members=Team.objects.filter().all()
        companyprofile=CompanyAbouts.objects.last()
        return render(request, self.template_name, {'team_members': team_members,'companyprofile':companyprofile})
        # return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


