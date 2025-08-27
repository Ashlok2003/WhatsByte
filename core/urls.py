from django.urls import path
from .views import (
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingPatientDetailView, MappingDeleteView
)

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient_list_create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('mappings/', MappingListCreateView.as_view(), name='mapping_list_create'),
    path('mappings/<int:patient_id>/', MappingPatientDetailView.as_view(), name='mapping_patient_detail'),
    path('mappings/<int:pk>/', MappingDeleteView.as_view(), name='mapping_delete'),
]
