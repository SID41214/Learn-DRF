
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


# Creating Router Object 
router = DefaultRouter()

# Register studentviewset with router
router.register('studentapi',views.StudentModelViewSet,basename='student') # only this required even for <int:pk> 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    
]
 