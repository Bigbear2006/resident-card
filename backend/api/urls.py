from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, 'categories')
router.register('events', views.EventViewSet, 'events')

urlpatterns = router.urls + [
    path('create-card/', views.CreateAPIView.as_view()),
    path('verify-passport/', views.VerifyPassportAPIView.as_view()),
]
