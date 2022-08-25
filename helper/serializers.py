from rest_framework import serializers
from .models import ProfileUser, Schemes, VolunteerProfile, AssistiveAids

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'address_line_1', 'address_line_2', 'city', 'state', 'pin_code', 'email', 'password', 'phone','disability_type', 'udid', 'caregiver_first_name', 'caregiver_middle_name', 'caregiver_last_name', 'caregiver_phone', 'caregiver_email')

class SchemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schemes
        fields = ('id', 'scheme_name', 'state', 'disability_benefits_criteria', 'benefit_types', 'document_link', 'summary', 'highlights' ,'disability_type')

class VolunteerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerProfile
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'address_line_1', 'address_line_2', 'city', 'state', 'pin_code', 'email', 'phone')

class AssistiveAidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistiveAids
        fields = ('id', 'name', 'price','vendor','location','disability_type')
