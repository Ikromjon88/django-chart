
from django.urls import path
from .views import*

urlpatterns = [
    path('', home),
    path('example/',example),
    path('linechart/',linechart), 
    path('piechart/', piechart),
    path('bubble/',bubble),
    path('area/', area),
]
