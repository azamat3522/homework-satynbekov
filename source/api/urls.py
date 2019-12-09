from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProjectViewset, TaskViewset, LogoutView

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewset)
router.register(r'tasks', TaskViewset)

app_name = 'api_v1'


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='obtain_auth_token'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),

]