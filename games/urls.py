from django.urls import path, include
from games import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'games', views.GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
