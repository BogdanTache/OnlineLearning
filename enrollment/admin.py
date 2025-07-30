from django.contrib import admin

from enrollment.models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_enrolled')
    list_filter = ('course', 'date_enrolled')
    search_fields = ('student__username', 'course__title')