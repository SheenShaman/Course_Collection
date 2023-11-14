from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from collection.models import Subscription
from collection.permissions import IsModerator, IsOwner
from collection.serializers import SubscriptionSerializer
from collection.services import send_sub_message


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """ Создание подписки """
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated | IsModerator | IsOwner]

    def perform_create(self, serializer):
        new_sub = serializer.save()
        new_sub.user = self.request.user
        new_sub.save()
        send_sub_message(new_sub.user.email, new_sub.course.title)


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """ Удаление подписки """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated | IsModerator | IsOwner]
