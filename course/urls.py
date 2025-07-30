from django.urls import path

from course import views

urlpatterns = [
    path('course_form', views.CourseCreateView.as_view(), name='course_form'),
    path('course_list', views.CourseListView.as_view(), name='course_list'),
    path('update_course/<int:pk>/', views.CourseUpdateView.as_view(), name='update_course'),
    path('course_detail/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course_delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('detalii_extra_course/<int:pk>/', views.CourseExtraDetailView.as_view(), name='detalii_extra_course'),
]