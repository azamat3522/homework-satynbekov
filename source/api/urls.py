from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewset, TaskViewset

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewset)
router.register(r'tasks', TaskViewset)

app_name = 'api_v1'


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]