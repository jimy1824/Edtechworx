from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Course
from home.models import HomeBanner
# from .forms import MyForm

class CoursesList(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'courses.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        courses=Course.objects.filter().all()
        return render(request, self.template_name, {'courses': courses})
        # return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


class CourseDetail(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'course-details.html'

    def get(self, request, course_id=None):
        # id=request.Get.get('course_id')
        print(course_id,'id')
        course_details = Course.objects.filter(id=course_id).first()
        courses=Course.objects.filter().all()
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'course_details': course_details,'courses':courses})
        # return render(request, self.template_name)


class CoursesEnrollment(View):
    # form_class = MyForm
    # initial = {'key': 'value'}
    template_name = 'enrollment.html'

    def get(self, request, course_id=None):
        homebanner = HomeBanner.objects.filter().last()
        # form = self.form_class(initial=self.initial)
        course_details = Course.objects.filter(id=course_id).first()
        return render(request, self.template_name, {'course_details': course_details,'homebanner':homebanner})
        # return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})
