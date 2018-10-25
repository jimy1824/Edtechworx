from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Gallery
# from .forms import MyForm

class GalleryView(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'gallery.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        gallery_images=Gallery.objects.filter().all()
        return render(request, self.template_name, {'gallery_images': gallery_images})
        # return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


