from django.urls import path

from instructor import views

urlpatterns = [
    path('create_instructor', views.InstructorCreateView.as_view(), name='create_instructor'),
    path('instructors_list', views.InstructorListView.as_view(), name='instructors_list'),
    path('detail_instructor/<int:pk>/', views.InstructorDetailView.as_view(), name='detail_instructor'),
    path('update_instructor/<int:pk>/', views.InstructorUpdateView.as_view(), name='update_instructor'),
    path('delete_instructor/<int:pk>/', views.InstructorDeleteView.as_view(), name='delete_instructor'),
]