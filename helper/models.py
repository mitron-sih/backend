from django.db import models

# Create your models here.

class disabilityType(models.Model):
    DIABILITY_TYPES = (
    ("1", "Blindness"),
    ("2", "Deaf"),
    
)
    disability_type=models.CharField(
        max_length = 20,
        choices = DIABILITY_TYPES,
        default = '1'
        )
    
    def __str__(self):
        return self.disability_type



class ProfileUser(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone=models.IntegerField()
    email=models.EmailField(max_length = 254)
    disability_type = models.ForeignKey(disabilityType, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name



class Schemes(models.Model):
    state=models.CharField(max_length=200)
    disability_benefits_criteria=models.IntegerField()
    benefit_types=models.CharField(max_length=500)
    document=models.URLField(max_length=200)
    summary=models.CharField(max_length=500)
    disability_type = models.ForeignKey(disabilityType, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.state


class VolunteerProfile(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    phone=models.IntegerField()

    def __str__(self):
        return self.name

class AssistiveAids(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    vendor=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    disability_type = models.ForeignKey(disabilityType, on_delete = models.CASCADE)
    


    def __str__(self):
        return self.name