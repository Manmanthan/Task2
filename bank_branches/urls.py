from django.urls import path, include
from rest_framework import routers

from bank_branches import views

router = routers.DefaultRouter()
router.register(r'banks', views.BankViewSet, views.BranchViewSet)
router.register(r'branches', views.BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]