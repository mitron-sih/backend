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
router.register(r'userLogin',views.UserLoginViewset)
router.register(r'volunteerLogin',views.VolunteerLoginViewset)
router.register(r'products',views.ProductsViewset)
router.register(r'requestedProducts',views.RequestedProductsViewset)
urlpatterns = router.urls
