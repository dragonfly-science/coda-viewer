from django.http import HttpResponse
from django.template import Context, loader


def variables(request, dataset):
    template = loader.get_template('variables.html')
    context = Context({'dataset': dataset})
    return HttpResponse(template.render(context))