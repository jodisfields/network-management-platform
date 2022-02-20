"""fisso_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from confman import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("ipam/", include("ipam.urls")),
    path("inventory/", include("inventory.urls")),
    path("confman/", include("confman.urls")),
    path("sites/", include("sites.urls")),
    path("tickets/", include("tickets.urls")),
    path("scripts/", include("scripts.urls")),
    path("topology/", include("topology.urls")),
    path("explorer/", include("explorer.urls")),
    path("documentation/", include("documentation.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]