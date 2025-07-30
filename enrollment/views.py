from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from enrollment.forms import EnrollmentForm
from enrollment.models import Enrollment


class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'enrollment/create_enrollment.html'
    model = Enrollment
    form_class = EnrollmentForm
    success_url = '/list_enrollment'

class EnrollmentListView(LoginRequiredMixin, ListView):
    template_name = 'enrollment/list_of_enrollment.html'
    model = Enrollment
    context_object_name = 'enrollments'


class EnrollmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'enrollment/update_enrollment.html'
    model = Enrollment
    form_class = EnrollmentForm
    success_url = '/list_enrollment'

class EnrollmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'enrollment/delete_enrollment.html'
    model = Enrollment
    success_url = '/list_enrollment'