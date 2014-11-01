from django.http.response import HttpResponse

# Create your views here.
from django.template import loader
from django.template.context import RequestContext
from home.compare import compare_cards


def index(request):
    template = loader.get_template('home/index.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))

def compare(request):
    first_card = request.GET['firstCard']
    second_card = request.GET['secondCard']

    return HttpResponse(compare_cards(first_card, second_card))