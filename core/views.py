import json

from django.shortcuts import render
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Profile
from core.permissions import IsOwnerProfileOrReadOnly
from core.serializers import ProfileSerializer


# Create your views here.

# class ProfileListCreateView(ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)
#
# class ProfileDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_profiles(request):
    if request.method == 'GET':
        queryset = Profile.objects.all().values()
        return Response({"data": queryset})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile(request, *args, **kwargs):
    if request.method == 'GET':
        queryset = Profile.objects.get(id=kwargs['profile_id'])
        data = ProfileSerializer(queryset).data
        return Response({"data": data})

    if request.method == 'PUT' and request.body is not None:
        queryset = Profile.objects.get(id=kwargs['profile_id'])
        data = ProfileSerializer(queryset, data=json.loads(request.body))
        print(data.is_valid())
        if data.is_valid():
            data.save()
        return Response({"data": 'sdfsdf'})
    # if request.method == 'PUT':
    #     pass




