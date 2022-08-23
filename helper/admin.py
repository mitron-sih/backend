from django.contrib import admin

# Register your models here.
from .models import ProfileUser,Schemes,VolunteerProfile,AssistiveAids
admin.site.register(ProfileUser)
admin.site.register(Schemes)
admin.site.register(VolunteerProfile)
admin.site.register(AssistiveAids)


