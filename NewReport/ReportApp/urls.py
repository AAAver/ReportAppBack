from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'run', views.RunViewSet)
router.register(r'test_results', views.TestResultViewSet)
router.register(r'attachments', views.AttachmentViewSet)


urlpatterns = [
    path('api/v0/', include(router.urls)),
    path('', views.HomePage, name='home_page'),
    path(r'uploadFiles/', views.FileFieldView.as_view())
]
