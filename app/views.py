from django.shortcuts import render
# step 1.1 import HttpResponse 
from django.http import HttpResponse, JsonResponse

# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    # return HttpResponse("Hello World")
    return render(request, 'index.html')

def listing(request):
    data = {"status":"success", "places":[{"id":"1","name":"Kyakt Taung Pagoda","cat_id":"1","lat":"22.014296","long":"96.447091"},{"id":"2","name":"Police Station","cat_id":"8","lat":"22.014722","long":"96.450895"},{"id":"3","name":"Famous Hotel","cat_id":"2","lat":"22.012989","long":"96.454909"},{"id":"4","name":"Lan San Aung Cafe","cat_id":"6","lat":"22.014854","long":"96.461379"},{"id":"5","name":"Junction(Ztwda)","cat_id":"7","lat":"22.016014","long":"96.467126"},{"id":"6","name":"Tai Puti Hotel (Daw Win)","cat_id":"2","lat":"22.01861","long":"96.464128"},{"id":"7","name":"No 4 Quarter Office","cat_id":"8","lat":"22.02094","long":"96.46303"},{"id":"8","name":"View Corner Restaurant","cat_id":"3","lat":"22.02394","long":"96.460295"},{"id":"9","name":"Sitta ThuKa Medicine Store","cat_id":"4","lat":"22.023381","long":"96.463702"},{"id":"10","name":"Htee Hlaing","cat_id":"8","lat":"22.016435","long":"96.469471"},{"id":"11","name":"Sabdar May Food","cat_id":"8","lat":"22.021061","long":"96.473173"},{"id":"12","name":"Nay La Thuka Hotel","cat_id":"2","lat":"22.023155","long":"96.468492"},{"id":"13","name":"KBZ Bank","cat_id":"5","lat":"22.026884","long":"96.4641"},{"id":"14","name":"Pin Se Cafe","cat_id":"6","lat":"22.028928","long":"96.465214"},{"id":"15","name":"Shwe Si Gone Junction","cat_id":"7","lat":"22.024692","long":"96.470421"},{"id":"16","name":"Mya NanTaw Hotel","cat_id":"2","lat":"22.022513","long":"96.474771"},{"id":"17","name":"Su PaungRestaurant","cat_id":"3","lat":"22.024068","long":"96.476552"},{"id":"18","name":"Shwe Kyal Store","cat_id":"4","lat":"22.026332","long":"96.470908"},{"id":"19","name":"Toyota U Than Shwe (Shop)","cat_id":"4","lat":"22.028505","long":"96.471483"},{"id":"20","name":"Sein Restaurant","cat_id":"3","lat":"22.028505","long":"96.47799"},{"id":"21","name":"Sandar Book Store","cat_id":"4","lat":"22.031904","long":"96.472356"},{"id":"22","name":"Shwe Moon Tyre Shop","cat_id":"4","lat":"22.032054","long":"96.476595"},{"id":"23","name":"Wing 2","cat_id":"8","lat":"22.009387","long":"96.454647"}]}
    return JsonResponse(data)