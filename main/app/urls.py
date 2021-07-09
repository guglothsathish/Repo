from django.urls import include, path
from rest_framework import routers
from app.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls, )),

]
