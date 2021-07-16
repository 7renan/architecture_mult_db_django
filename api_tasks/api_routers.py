from rest_framework import routers
from rest_framework.routers import DefaultRouter

# views
from tasks import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')

api_routers = router.urls



