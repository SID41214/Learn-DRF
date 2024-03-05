
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/',views.StudentList.as_view()),
    # path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/',views.StudentLC.as_view()),
   
   
   
    path('studentapi/',views.StudentLC.as_view()),
    
    
    



    # path('studentapi/<int:pk>',views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>',views.StudentDestroy.as_view()),
    # path('studentapi/<int:pk>',views.StudentRU.as_view()),
    # path('studentapi/<int:pk>',views.StudentRD.as_view()),
    # path('studentapi/<int:pk>',views.StudentRUD.as_view()),


    path('studentapi/<int:pk>',views.StudentRUD.as_view()),

    
   
    
    
]
