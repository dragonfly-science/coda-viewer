from django.http import HttpResponse
from django.template import Context, loader

import codaaccess


def variables(request, dataset):
    template = loader.get_template('variables.html')
    variables_list = codaaccess.variables(dataset)
    context = Context({'dataset': dataset, 'variables': variables_list})
    return HttpResponse(template.render(context))
   
    
def trace(request, dataset, variable):
    'renders a trace plot (hairy caterpiller) for the specified variable'
    template = loader.get_template('trace.html')
    context = Context({'dataset': dataset, 'variable': variable})
    return HttpResponse(template.render(context))

def overview(request, dataset):
    'returns a single page app which provides a visual overview of the dataset'
    template = loader.get_template('overview.html')
    return HttpResponse(template.render(Context({'dataset': dataset})))