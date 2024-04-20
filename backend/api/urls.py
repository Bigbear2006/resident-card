from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, 'categories')
router.register('events', views.EventViewSet, 'events')
router.register('hospitals', views.HospitalViewSet, 'hospitals')
router.register('banks', views.BankViewSet, 'banks')
router.register('cards', views.CardViewSet, 'cards')

urlpatterns = router.urls + [
    path('buy-ticket/', views.BuyTicketAPIView.as_view()),
    path('verify-passport/', views.VerifyPassportAPIView.as_view()),
]
