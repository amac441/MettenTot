from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html')
        #takes a parameter, request, which is an object that has information about the 
        #user requesting the page from the browser. 
        #The function's response is to simply render the index.html template