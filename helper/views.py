from django.shortcuts import render
from rest_framework import viewsets 
from googletrans import Translator, constants
# Create your views here.

from .models import ProfileUser,Schemes,VolunteerProfile,AssistiveAids, Products, RequestedProducts
from .serializers import ProfileSerializer,SchemesSerializer,VolunteerProfileSerializer,AssistiveAidsSerializer, ProductsSerializer, RequestedProductsSerializer
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileSerializer


class SchemesViewSet(viewsets.ModelViewSet):

    serializer_class = SchemesSerializer
    def get_queryset(self):
        queryset = Schemes.objects.all()
        lang = self.request.query_params.get('lang')
        disability_type = self.request.query_params.get('dt')
        if(disability_type):
            queryset = queryset.filter(disability_type=disability_type)
        if(lang and lang != 'en'):
            for scheme in queryset:
                scheme.scheme_name = Translator().translate(scheme.scheme_name, lang).text
                scheme.state = Translator().translate(scheme.state, lang).text
                scheme.disability_benefits_criteria = Translator().translate(scheme.disability_benefits_criteria, lang).text
                scheme.benefit_types = Translator().translate(scheme.benefit_types, lang).text
                scheme.summary = Translator().translate(scheme.summary, lang).text
                sh = ""
                scheme.highlights = scheme.highlights.split('. ')
                for idx, highlight in enumerate(scheme.highlights):
                    sh += Translator().translate(highlight, lang).text + "#"
                scheme.highlights = sh
        return queryset
    queryset = Schemes.objects.all()


class VolunteerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerProfileSerializer
    def get_queryset(self):
        queryset = VolunteerProfile.objects.all()
        pin_code = self.request.query_params.get('pin_code')
        if pin_code is not None:
            queryset = queryset.filter(pin_code=pin_code)
        return queryset

    queryset = VolunteerProfile.objects.all()
    

class AssistiveAidsViewSet(viewsets.ModelViewSet):
    queryset=AssistiveAids.objects.all()
    serializer_class=AssistiveAidsSerializer

class UserLoginViewset(viewsets.ModelViewSet):
    queryset=ProfileUser.objects.all()
    serializer_class = ProfileSerializer
    def get_queryset(self):
        queryset = ProfileUser.objects.all()
        email = self.request.query_params.get('email')
        password = self.request.query_params.get('password')
        if email and password:
            queryset = queryset.filter(email=email)
            queryset = queryset.filter(password=password)
        return queryset

class VolunteerLoginViewset(viewsets.ModelViewSet):
    queryset=VolunteerProfile.objects.all()
    serializer_class = VolunteerProfileSerializer
    def get_queryset(self):
        queryset = VolunteerProfile.objects.all()
        email = self.request.query_params.get('email')
        password = self.request.query_params.get('password')
        if email and password:
            queryset = queryset.filter(email=email)
            queryset = queryset.filter(password=password)
        return queryset

class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
class RequestedProductsViewset(viewsets.ModelViewSet):
    queryset = RequestedProducts.objects.all()
    serializer_class = RequestedProductsSerializer