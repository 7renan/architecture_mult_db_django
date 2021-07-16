from django.contrib import admin
from django.urls import path, include

# routers api
from .api_routers import api_routers

urlpatterns = [
    path('api/', include(api_routers)),
    path('admin/', admin.site.urls),
]
