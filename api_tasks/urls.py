from django.contrib import admin
from django.urls import path, include
from core.views import api_redirect

# routers api
from .api_routers import api_routers

urlpatterns = [
    path('', api_redirect),
    path('api/', include(api_routers)),
    path('admin/', admin.site.urls),
]
