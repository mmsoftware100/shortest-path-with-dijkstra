from django.shortcuts import render
# step 1.1 import HttpResponse 
from django.http import HttpResponse

# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    return HttpResponse("Hello World")