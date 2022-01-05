from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('faculty_training',views.faculty_training, name="faculty_training"),
   path('patents',views.patents, name="patents"),
   path('publications',views.publications, name="publications"),
   path('invited_talks',views.invited_talks, name="invited_talks"),
   path('inhouse_project',views.inhouse_project, name="inhouse_project"),
   path('consultancy_projects',views.consultancy_projects, name="consultancy_projects"),
]

