# not sure if this is really an api yet :)

from django.http import HttpResponse
from ..codaaccess import get_data as get_coda_data, variables

import json
import numpy 


# TODO: risto ~ Wed Mar 13 15:55:48 NZDT 2013 >>>
# add ?dtype=float64 type of functionality, and possibly filtering and windowing
def get_data(request, dataset, variable):
    rawdata = get_coda_data(dataset, variable)
    # rawdata is float32
    arraybuffer = buffer(rawdata)
    response = HttpResponse(mimetype="image/png")
    response.write(arraybuffer)
    return response
    
def get_variable_list(request, dataset):
    varlist = variables(dataset)
    return HttpResponse(json.dumps(varlist), mimetype='application/json')