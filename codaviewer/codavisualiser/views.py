from django.http import HttpResponse
from django.template import Context, loader

import codaaccess


def variables(request, dataset):
    template = loader.get_template('variables.html')
    variables_list = codaaccess.variables(dataset)
    context = Context({'dataset': dataset, 'variables': variables_list})
    return HttpResponse(template.render(context))