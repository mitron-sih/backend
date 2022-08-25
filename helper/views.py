from django.shortcuts import render
from rest_framework import viewsets 
# Create your views here.

from .models import ProfileUser,Schemes,VolunteerProfile,AssistiveAids
from .serializers import ProfileSerializer,SchemesSerializer,VolunteerProfileSerializer,AssistiveAidsSerializer
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileSerializer


class SchemesViewSet(viewsets.ModelViewSet):
    queryset = Schemes.objects.all()
    serializer_class = SchemesSerializer


class VolunteerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerProfileSerializer
    def get_queryset(self):
        queryset = VolunteerProfile.objects.all()
        city = self.request.query_params.get('city')
        print("city", city)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset

    queryset = VolunteerProfile.objects.all()
    

class AssistiveAidsViewSet(viewsets.ModelViewSet):
    queryset=AssistiveAids.objects.all()
    serializer_class=AssistiveAidsSerializer
