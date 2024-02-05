from django.urls import path
from .views import *
urlpatterns = [
    path('MovieList/',MovieList.as_view(),name='Movie_List'), 
    path('MovieDetail/<int:pk>', MovieDetail.as_view(), name='Movie_Detail')
]     