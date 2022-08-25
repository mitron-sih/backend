from django.db import models

# Create your models here.

def getDisabilityTypes():
    return [
        ("1", "Hearing Impairment"),
        ("2", "Autism"),
        ("3", "Leprosy"),
        ("4", "Intellectual Disability"),
        ("5", "Complete Blindness"),
        ("6", "Person With Low Vision"),
        ("7", "Handicapped"),
        ("8", "Dyslexia"),
        ("9", "Cerebral Palsy"),
        ("10", "Locomotor Disability")
    ]

class ProfileUser(models.Model):    

    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    address_line_1 = models.CharField(max_length = 150)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    pin_code = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 30)
    disability_type = models.CharField(max_length = 20, choices = getDisabilityTypes(), default = '1')
    udid = models.CharField(max_length = 50)
    caregiver_first_name = models.CharField(max_length = 25)
    caregiver_last_name = models.CharField(max_length = 25)
    caregiver_phone = models.IntegerField()
    caregiver_email = models.EmailField(max_length = 254)
    
    def __str__(self):
        return self.name



class Schemes(models.Model):

    scheme_name = models.CharField(max_length = 150)
    state = models.CharField(max_length = 50)
    disability_benefits_criteria = models.CharField(max_length = 100)
    benefit_types = models.CharField(max_length = 100)
    document_link = models.URLField(max_length = 200)
    summary = models.CharField(max_length=2000)
    highlights = models.CharField(max_length=5000)
    disability_type = models.CharField(max_length = 20, choices = getDisabilityTypes(), default = '1')
    

    def __str__(self):
        return self.state


class VolunteerProfile(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    address_line_1 = models.CharField(max_length = 150)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    pin_code = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length = 254)
    phone=models.IntegerField()
    aadhar_number=models.CharField(max_length=12)

    def __str__(self):
        return self.first_name

class AssistiveAids(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    vendor=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    disability_type = models.CharField(max_length = 20, choices = getDisabilityTypes(), default = '1')
    
    def __str__(self):
        return self.name
