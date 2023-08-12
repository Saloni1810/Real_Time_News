from django.urls import path
from . import views

urlpatterns = [
    path('',views.allnews,name="headlines"),
    path('allnews',views.allnews,name="allnews"),
    path('topnews',views.topnews,name="topnews"),
    path('trendingnews',views.trendingnews,name="trendingnews"),
    path('sportsnews',views.sportsnews,name="sportsnews"),
    path('sciencenews',views.sciencenews,name="sciencenews"),
    path('entnews',views.entnews,name="entnews")

]