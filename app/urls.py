from django.urls import path
from . import views

urlpatterns = [
    # add first element to urlpatterns array
    # path function accept two parameter
    # first parameter is url path
    # second parameter is function name 
    path("", views.splash),
    path("index", views.index),
    path("listing", views.listing),
    path("graph", views.graph),
    path("calculate", views.calculate),

    path("about", views.about_page),
    path("home", views.home_page),
    path("places", views.places_page),
    path("result", views.result_page),
    path("search", views.search_page),
    path("start", views.start_page),
]