import json
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
    return HttpResponse(json.dumps(data))
    # return JsonResponse(data)

def graph(request):
    data = {"status":"success","misc":"{\"operation\":\"get_graph\"}","places":[{"id":"1","name":"Kyakt Taung Pagoda","cat_id":"1","lat":"22.014296","long":"96.447091"},{"id":"2","name":"Police Station","cat_id":"8","lat":"22.014722","long":"96.450895"},{"id":"3","name":"Famous Hotel","cat_id":"2","lat":"22.012989","long":"96.454909"},{"id":"4","name":"Lan San Aung Cafe","cat_id":"6","lat":"22.014854","long":"96.461379"},{"id":"5","name":"Junction(Ztwda)","cat_id":"7","lat":"22.016014","long":"96.467126"},{"id":"6","name":"Tai Puti Hotel (Daw Win)","cat_id":"2","lat":"22.01861","long":"96.464128"},{"id":"7","name":"No 4 Quarter Office","cat_id":"8","lat":"22.02094","long":"96.46303"},{"id":"8","name":"View Corner Restaurant","cat_id":"3","lat":"22.02394","long":"96.460295"},{"id":"9","name":"Sitta ThuKa Medicine Store","cat_id":"4","lat":"22.023381","long":"96.463702"},{"id":"10","name":"Htee Hlaing","cat_id":"8","lat":"22.016435","long":"96.469471"},{"id":"11","name":"Sabdar May Food","cat_id":"8","lat":"22.021061","long":"96.473173"},{"id":"12","name":"Nay La Thuka Hotel","cat_id":"2","lat":"22.023155","long":"96.468492"},{"id":"13","name":"KBZ Bank","cat_id":"5","lat":"22.026884","long":"96.4641"},{"id":"14","name":"Pin Se Cafe","cat_id":"6","lat":"22.028928","long":"96.465214"},{"id":"15","name":"Shwe Si Gone Junction","cat_id":"7","lat":"22.024692","long":"96.470421"},{"id":"16","name":"Mya NanTaw Hotel","cat_id":"2","lat":"22.022513","long":"96.474771"},{"id":"17","name":"Su PaungRestaurant","cat_id":"3","lat":"22.024068","long":"96.476552"},{"id":"18","name":"Shwe Kyal Store","cat_id":"4","lat":"22.026332","long":"96.470908"},{"id":"19","name":"Toyota U Than Shwe (Shop)","cat_id":"4","lat":"22.028505","long":"96.471483"},{"id":"20","name":"Sein Restaurant","cat_id":"3","lat":"22.028505","long":"96.47799"},{"id":"21","name":"Sandar Book Store","cat_id":"4","lat":"22.031904","long":"96.472356"},{"id":"22","name":"Shwe Moon Tyre Shop","cat_id":"4","lat":"22.032054","long":"96.476595"},{"id":"23","name":"Wing 2","cat_id":"8","lat":"22.009387","long":"96.454647"}],"links":[{"id":"1","node1":"1","node2":"2","distance":"410"},{"id":"2","node1":"1","node2":"8","distance":"1755"},{"id":"3","node1":"2","node2":"3","distance":"455"},{"id":"4","node1":"2","node2":"7","distance":"1490"},{"id":"5","node1":"3","node2":"4","distance":"705"},{"id":"6","node1":"4","node2":"5","distance":"616"},{"id":"7","node1":"4","node2":"6","distance":"510"},{"id":"8","node1":"5","node2":"6","distance":"395"},{"id":"9","node1":"5","node2":"10","distance":"255"},{"id":"10","node1":"6","node2":"7","distance":"290"},{"id":"11","node1":"7","node2":"8","distance":"425"},{"id":"12","node1":"7","node2":"9","distance":"322"},{"id":"13","node1":"8","node2":"9","distance":"335"},{"id":"14","node1":"8","node2":"13","distance":"482"},{"id":"15","node1":"9","node2":"12","distance":"700"},{"id":"16","node1":"9","node2":"13","distance":"388"},{"id":"17","node1":"10","node2":"11","distance":"655"},{"id":"18","node1":"11","node2":"12","distance":"503"},{"id":"19","node1":"11","node2":"16","distance":"255"},{"id":"20","node1":"12","node2":"15","distance":"251"},{"id":"21","node1":"13","node2":"14","distance":"235"},{"id":"22","node1":"14","node2":"18","distance":"668"},{"id":"23","node1":"14","node2":"21","distance":"878"},{"id":"24","node1":"15","node2":"18","distance":"201"},{"id":"25","node1":"16","node2":"17","distance":"305"},{"id":"26","node1":"17","node2":"18","distance":"643"},{"id":"27","node1":"17","node2":"20","distance":"363"},{"id":"28","node1":"18","node2":"19","distance":"220"},{"id":"29","node1":"19","node2":"20","distance":"1080"},{"id":"30","node1":"19","node2":"21","distance":"362"},{"id":"36","node1":"20","node2":"22","distance":"543"},{"id":"37","node1":"21","node2":"22","distance":"419"},{"id":"38","node1":"23","node2":"3","distance":"200"},{"id":"39","node1":"16","node2":"15","distance":"550"}]}
    return HttpResponse(json.dumps(data)) 

def calculate(request):
    # get source_id and destination id
    # Retrieve GET parameters with default values
    source_id = request.GET.get('source_id', 0)
    destination_id = request.GET.get('destination_id', 0)
    # return HttpResponse(destination_id)

    # Graph

    # calculate result

    data = {"status":"success","misc":"{\"operation\":\"shortest_path\",\"source_id\":\"1\",\"destination_id\":\"15\"}","links":[{"id":"1","node1":"1","node2":"2","distance":"410"},{"id":"2","node1":"1","node2":"8","distance":"1755"},{"id":"3","node1":"2","node2":"3","distance":"455"},{"id":"4","node1":"2","node2":"7","distance":"1490"},{"id":"5","node1":"3","node2":"4","distance":"705"},{"id":"6","node1":"4","node2":"5","distance":"616"},{"id":"7","node1":"4","node2":"6","distance":"510"},{"id":"8","node1":"5","node2":"6","distance":"395"},{"id":"9","node1":"5","node2":"10","distance":"255"},{"id":"10","node1":"6","node2":"7","distance":"290"},{"id":"11","node1":"7","node2":"8","distance":"425"},{"id":"12","node1":"7","node2":"9","distance":"322"},{"id":"13","node1":"8","node2":"9","distance":"335"},{"id":"14","node1":"8","node2":"13","distance":"482"},{"id":"15","node1":"9","node2":"12","distance":"700"},{"id":"16","node1":"9","node2":"13","distance":"388"},{"id":"17","node1":"10","node2":"11","distance":"655"},{"id":"18","node1":"11","node2":"12","distance":"503"},{"id":"19","node1":"11","node2":"16","distance":"255"},{"id":"20","node1":"12","node2":"15","distance":"251"},{"id":"21","node1":"13","node2":"14","distance":"235"},{"id":"22","node1":"14","node2":"18","distance":"668"},{"id":"23","node1":"14","node2":"21","distance":"878"},{"id":"24","node1":"15","node2":"18","distance":"201"},{"id":"25","node1":"16","node2":"17","distance":"305"},{"id":"26","node1":"17","node2":"18","distance":"643"},{"id":"27","node1":"17","node2":"20","distance":"363"},{"id":"28","node1":"18","node2":"19","distance":"220"},{"id":"29","node1":"19","node2":"20","distance":"1080"},{"id":"30","node1":"19","node2":"21","distance":"362"},{"id":"36","node1":"20","node2":"22","distance":"543"},{"id":"37","node1":"21","node2":"22","distance":"419"},{"id":"38","node1":"23","node2":"3","distance":"200"},{"id":"39","node1":"16","node2":"15","distance":"550"}],"solution":{"status":"route","distance":3041,"solution_path":["1",8,9,12,"15"]},"places":[{"id":"1","name":"Kyakt Taung Pagoda","cat_id":"1","lat":"22.014296","long":"96.447091"},{"id":"2","name":"Police Station","cat_id":"8","lat":"22.014722","long":"96.450895"},{"id":"3","name":"Famous Hotel","cat_id":"2","lat":"22.012989","long":"96.454909"},{"id":"4","name":"Lan San Aung Cafe","cat_id":"6","lat":"22.014854","long":"96.461379"},{"id":"5","name":"Junction(Ztwda)","cat_id":"7","lat":"22.016014","long":"96.467126"},{"id":"6","name":"Tai Puti Hotel (Daw Win)","cat_id":"2","lat":"22.01861","long":"96.464128"},{"id":"7","name":"No 4 Quarter Office","cat_id":"8","lat":"22.02094","long":"96.46303"},{"id":"8","name":"View Corner Restaurant","cat_id":"3","lat":"22.02394","long":"96.460295"},{"id":"9","name":"Sitta ThuKa Medicine Store","cat_id":"4","lat":"22.023381","long":"96.463702"},{"id":"10","name":"Htee Hlaing","cat_id":"8","lat":"22.016435","long":"96.469471"},{"id":"11","name":"Sabdar May Food","cat_id":"8","lat":"22.021061","long":"96.473173"},{"id":"12","name":"Nay La Thuka Hotel","cat_id":"2","lat":"22.023155","long":"96.468492"},{"id":"13","name":"KBZ Bank","cat_id":"5","lat":"22.026884","long":"96.4641"},{"id":"14","name":"Pin Se Cafe","cat_id":"6","lat":"22.028928","long":"96.465214"},{"id":"15","name":"Shwe Si Gone Junction","cat_id":"7","lat":"22.024692","long":"96.470421"},{"id":"16","name":"Mya NanTaw Hotel","cat_id":"2","lat":"22.022513","long":"96.474771"},{"id":"17","name":"Su PaungRestaurant","cat_id":"3","lat":"22.024068","long":"96.476552"},{"id":"18","name":"Shwe Kyal Store","cat_id":"4","lat":"22.026332","long":"96.470908"},{"id":"19","name":"Toyota U Than Shwe (Shop)","cat_id":"4","lat":"22.028505","long":"96.471483"},{"id":"20","name":"Sein Restaurant","cat_id":"3","lat":"22.028505","long":"96.47799"},{"id":"21","name":"Sandar Book Store","cat_id":"4","lat":"22.031904","long":"96.472356"},{"id":"22","name":"Shwe Moon Tyre Shop","cat_id":"4","lat":"22.032054","long":"96.476595"},{"id":"23","name":"Wing 2","cat_id":"8","lat":"22.009387","long":"96.454647"}]}
    return HttpResponse(json.dumps(data)) 