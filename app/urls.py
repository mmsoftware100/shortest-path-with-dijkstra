from django.urls import path
from . import views

urlpatterns = [
    # add first element to urlpatterns array
    # path function accept two parameter
    # first parameter is url path
    # second parameter is function name 
    path("", views.splash),
    path("home", views.static_home),
    path("about", views.static_about),
    path("places", views.static_places),
    path("result", views.static_result),
    path("search", views.static_search),


    path("index", views.index),
    path("listing", views.listing),
    path("graph", views.do_graph),
    path("calculate", views.calculate),
]