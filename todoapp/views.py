from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Task


def index(request):
    task_list = Task.objects.order_by('frist')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'task_list': task_list,
    })
    return HttpResponse(template.render(context))