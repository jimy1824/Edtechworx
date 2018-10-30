from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Blogs,BlogBanner
# from .forms import MyForm

class BlogList(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        blogs=Blogs.objects.filter().all()
        blogbanner=BlogBanner.objects.last()
        return render(request, self.template_name, {'blogs': blogs,'blogbanner':blogbanner})
        # return render(request, self.template_name)

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

    def get(self, request, blog_id=None):
        # form = self.form_class(initial=self.initial)
        blog_detail=Blogs.objects.filter(id=blog_id).first()
        return render(request, self.template_name, {'blog_detail': blog_detail})
        # return render(request, self.template_name)