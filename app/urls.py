# company/urls.py

from django.urls import path
from .views import DeptViewSet, EmpViewSet

department_list = DeptViewSet.as_view({'get': 'list', 'post': 'create'})
department_detail = DeptViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

employee_list = EmpViewSet.as_view({'get': 'list', 'post': 'create'})
employee_detail = EmpViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = [
    path('api/departments/', department_list, name='department-list'),
    path('api/departments/<int:pk>/', department_detail, name='department-detail'),
    path('api/employees/', employee_list, name='employee-list'),
    path('api/employees/<int:pk>/', employee_detail, name='employee-detail'),
]
