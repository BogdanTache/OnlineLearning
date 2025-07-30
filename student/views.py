import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from course.models import Course
from enrollment.models import Enrollment
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student
from userextend.models import UserExtend


class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = '/create_student/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        context['curent_datetime'] = now

        return context



class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/list_of_student.html'
    model = Student
    context_object_name = 'students_list'


    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_user'] = UserExtend.objects.get(user_ptr_id=self.request.user.id)

        return context



class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = '/list_students/'



class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'student/detail_student.html'
    model = Student


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = '/list_students/'

