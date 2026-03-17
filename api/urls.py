from django.urls import path, include
from api.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', EmployeeViewSet)


urlpatterns = [
    #path('employees/', EmployeeList.as_view()),
    #path('employee/<int:pk>/', EmployeeDetail.as_view()),
    
    path('', include(router.urls))
]
