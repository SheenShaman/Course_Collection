from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from collection.models import Course, Subscription
from collection.paginators import CoursePaginator
from collection.permissions import IsModerator, IsOwner
from collection.serializers import CourseSerializer, CourseCreateSerializer
from collection.tasks import send_update_course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated | IsModerator | IsOwner]
    pagination_class = CoursePaginator

    def create(self, request, *args, **kwargs):
        serializer = CourseCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()
        return Response(CourseCreateSerializer(new_course).data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.last_updated = timezone.now()
        instance.save()

        subscriptions = Subscription.objects.filter(
            course=instance,
            is_active=True
        )
        user_emails = [subscription.user.email for subscription in subscriptions]
        send_update_course.delay(instance.name, user_emails)
