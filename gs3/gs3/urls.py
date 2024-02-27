
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.student_api),
    #path('studentapi/',views.StudentAPI.as_view()),   >>if class is used 
]
