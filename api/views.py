
from .permissions import isOwner
from restaurants.models import Restaurant
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantCreateUpdateSerializer,
)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permissions_class = [AllowAny]


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    permissions_class = [AllowAny]


class RestaurantCreateView(CreateAPIView):
    serializer_class = RestaurantCreateUpdateSerializer
    permissions_class = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RestaurantUpdateView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    permissions_class = [isOwner, IsAdminUser]
    serializer_class = RestaurantCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    


class RestaurantDeleteView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permissions_class = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'