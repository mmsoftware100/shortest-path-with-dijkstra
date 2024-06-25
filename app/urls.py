from django.urls import path
from . import views

urlpatterns = [
    # add first element to urlpatterns array
    # path function accept two parameter
    # first parameter is url path
    # second parameter is function name 
    path("", views.splash),
    path("home", views.static_home),


    path("index", views.index),
    path("listing", views.listing),
    path("graph", views.graph),
    path("calculate", views.calculate),
]