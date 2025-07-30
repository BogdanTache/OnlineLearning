from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from course.models import Course
from instructor.forms import InstructorForm, InstructorUpdateForm
from instructor.models import Instructor


class InstructorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'instructor/create_instructor.html'
    model = Instructor
    form_class = InstructorForm
    success_url = '/instructors_list'



class InstructorListView(LoginRequiredMixin, ListView):
    template_name = 'instructor/list_of_instructors.html'
    model = Instructor
    context_object_name = 'instructors_list'


class InstructorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'instructor/update_instructor.html'
    model = Instructor
    form_class = InstructorUpdateForm
    success_url = '/instructors_list'

class InstructorDetailView(LoginRequiredMixin, DetailView):
    template_name = 'instructor/detail_instructor.html'
    model = Instructor



class InstructorDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'instructor/delete_instructor.html'
    model = Instructor
    success_url = '/instructors_list'
