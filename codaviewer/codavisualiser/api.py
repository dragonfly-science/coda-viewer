# not sure if this is really an api yet :)

from django.http import HttpResponse
import codaaccess

import json
import numpy 


# TODO: risto ~ Wed Mar 13 15:55:48 NZDT 2013 >>>
# add ?dtype=float64 type of functionality, and possibly filtering and windowing
def get_data(request, dataset, variable):
    rawdata = codaaccess.get_data(dataset, variable)
    # rawdata is float32
    arraybuffer = buffer(rawdata)
    response = HttpResponse(mimetype="image/png")
    response.write(arraybuffer)
    return response