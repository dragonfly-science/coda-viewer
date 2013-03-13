# not sure if this is really an api yet :)

from django.http import HttpResponse
import codaacess

import json

def variables(request, dataset):
    data = json.dumps(codaaccess.variables(dataset))
    return HttpResponse(data, mimetype='application/json')