from django.conf import settings
from codaparser import CodaResults

def django_accessed_dataset(dataset):
    datadir = '%s/%s'% (settings.DATADIR, dataset)
    return CodaResults(datadir)
    
    
def variables(dataset):
    coda = django_accessed_dataset(dataset)
    return coda.variables


def get_data(dataset, variable):
    coda = django_accessed_dataset(dataset)
    return coda.get_data(variable)
        