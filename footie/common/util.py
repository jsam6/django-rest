
from django.http import HttpResponse, HttpResponseBadRequest
import json 

def response(data, code):
    if code == 200:
        return HttpResponse(json.dumps(data), content_type="application/json")
    elif code == 401:
        return HttpResponseBadRequest(data, content_type="application/json")