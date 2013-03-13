# not sure if this is really an api yet :)

from django.http import HttpResponse
from django.conf import settings
from codaparser import CodaResults

import json

def variables(request, dataset):
    datadir = '%s/%s'% (settings.DATADIR, dataset)
    coda = CodaResults(datadir)
    data = json.dumps(coda.variables)
    return HttpResponse(data, mimetype='application/json')