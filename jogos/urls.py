
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JogoViewSet

router = DefaultRouter()
router.register(r'jogos', JogoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
