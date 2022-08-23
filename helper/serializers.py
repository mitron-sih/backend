from rest_framework import serializers
from .models import ProfileUser,Schemes,VolunteerProfile,AssistiveAids

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('id', 'name', 'address','phone','email','disability_type')

class SchemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schemes
        fields = ('id', 'state', 'disability_benefits_criteria','benefit_types','document','summary','disability_type')

class VolunteerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerProfile
        fields = ('id', 'name', 'location','phone')

class AssistiveAidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistiveAids
        fields = ('id', 'name', 'price','vendor','location','disability_type')