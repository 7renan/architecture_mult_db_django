from rest_framework import routers
from rest_framework.routers import DefaultRouter

# views
from tasks.views import TaskViewSet
from tenants.views import TenantViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
router.register('tenants', TenantViewSet, basename='tenants')

api_routers = router.urls



