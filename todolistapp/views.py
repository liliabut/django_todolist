from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Task

def index(request):
    latest_tasks_list = Task.objects.order_by('-due_date')[:5]
    template = loader.get_template('index.html')
    
    context = RequestContext(request, {
        'latest_tasks_list': latest_tasks_list,
    })
    
    return HttpResponse(template.render(context))