from django.urls import path

from enrollment import views

urlpatterns = [
    path('create_enrollment/', views.EnrollmentCreateView.as_view(), name='create_enrollment'),
    path('list_enrollment/', views.EnrollmentListView.as_view(), name='list_enrollment'),
    path('update_enrollment/<int:pk>/', views.EnrollmentUpdateView.as_view(), name='update_enrollment'),
    path('delete_enrollment/<int:pk>/', views.EnrollmentDeleteView.as_view(), name='delete_enrollment'),

]