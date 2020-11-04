from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateAPIView
from rest_framework.response import Response

from .serializers import NeighbourhoodSerializer, UserSerializer, ProfileSerializer
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
    lookup_field = 'pk'

    def get_object(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(Neighbourhood, pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('userid'))
        return serializer.save(user=user)

class SingleUserView(RetrieveUpdateAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_object(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(User, pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class ProfileView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer