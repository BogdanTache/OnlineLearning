from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from course.forms import CourseForm
from course.models import Course


class CourseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'course/course_form.html'
    model = Course
    form_class = CourseForm
    success_url = '/course_list'


class CourseListView(LoginRequiredMixin, ListView):
    template_name = 'course/course_list.html'
    model = Course
    context_object_name = 'course_list'


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'course/update_course.html'
    model = Course
    form_class = CourseForm
    success_url = '/course_list'


class CourseDetailView(LoginRequiredMixin, DetailView):
    template_name = 'course/course_detail.html'
    model = Course


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'course/course_delete.html'
    model = Course
    success_url = '/course_list'


class CourseExtraDetailView(DetailView):
    template_name = 'course/detalii_extra_course.html'
    model = Course
