from django.http.response import HttpResponse

# Create your views here.
from django.template import loader
from django.template.context import RequestContext


def index(request):
    template = loader.get_template('home/index.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))