
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter


# Creating Router Object 
router = DefaultRouter()

# Register studentviewset with router
router.register('studentapi',views.StudentModelViewSet,basename='student') # only this required even for <int:pk> 
# router.register('studentapi/<int:pk>',views.StudentViewSet,basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
 