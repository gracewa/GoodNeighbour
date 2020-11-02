from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateAPIView
from rest_framework.response import Response

from .serializers import NeighbourhoodSerializer, UserSerializer
from ..models import Neighbourhood, Business, EmergencyService, Profile
from django.contrib.auth.models import User


class NeighbourhoodView(ListCreateAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = NeighbourhoodSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('userid'))
        return serializer.save(user=user)

class SingleNeighbourhoodView(RetrieveUpdateAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = NeighbourhoodSerializer

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('userid'))
        return serializer.save(user=user)

class SingleUserView(RetrieveUpdateAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = UserSerializer