from django.urls import path

from collection.apps import CollectionConfig
from rest_framework.routers import DefaultRouter

from collection.views.views_courses import CourseViewSet
from collection.views.views_subscriptions import SubscriptionCreateAPIView, SubscriptionDestroyAPIView
from collection.views.views_lessons import (LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView,
                                            LessonUpdateAPIView, LessonDestroyAPIView)

app_name = CollectionConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('sub/create/', SubscriptionCreateAPIView.as_view(), name='sub_create'),
    path('sub/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='sub_delete'),
] + router.urls
