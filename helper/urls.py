from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from helper import views
import re
router=routers.DefaultRouter()


router.register(r'user',views.ProfileViewSet)
router.register(r'schemes',views.SchemesViewSet)
router.register(r'volunteer',views.VolunteerProfileViewSet)
router.register(r'aids',views.AssistiveAidsViewSet)
# router.register('user',ProfileViewSet,base_name='users')
urlpatterns = router.urls
# path('scheme<int:pk>/',DetailedListSchemes.as_view()),
# path('scheme', ListSchemes.as_view()),
# path('volunteer<int:pk>/',DetailedVolunteerProfile.as_view()),
# path('volunteer', VolunteerProfileList.as_view()),
# path('aids<int:pk>/',DetailedAssistiveAids.as_view()),
# path('aids', AssistiveAidsList.as_view()),
