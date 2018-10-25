from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# from .forms import MyForm

class BlogList(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


class BlogDetail(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'blog-single.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)