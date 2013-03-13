from django.conf import settings
from codaparser import CodaResults

def variables(dataset):
    datadir = '%s/%s'% (settings.DATADIR, dataset)
    coda = CodaResults(datadir)
    return coda.variables
    