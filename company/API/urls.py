from django.urls import path
from API import views

urlpatterns = (
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-details'),
    path('employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-details'),
)