from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from collection.models import Subscription
from collection.permissions import IsModerator, IsOwner
from collection.serializers import SubscriptionSerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated | IsModerator | IsOwner]


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated | IsModerator | IsOwner]