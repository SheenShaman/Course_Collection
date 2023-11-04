from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from collection.models import Course, Subscription
from collection.paginators import CoursePaginator
from collection.permissions import IsModerator, IsOwner
from collection.serializers import CourseSerializer, CourseCreateSerializer
from collection.services import send_sub_message


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

    def partial_update(self, request, pk=None, **kwargs):
        course = self.get_object()
        serializer = self.get_serializer(course, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        user = self.request.user
        subscription = Subscription.objects.filter(user=user, course=course, is_active=True)
        if subscription:
            send_sub_message(user.email, course.title)
        return Response(serializer.data)
