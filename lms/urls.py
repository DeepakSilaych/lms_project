from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ClassViewSet, AssignmentViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]