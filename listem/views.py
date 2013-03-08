from django.template import Context, loader
from listem.models import Lists
from django.http import HttpResponse

def index(request):
	latest_lists_list = Lists.objects.all().order_by('-created')[:5]
	t = loader.get_template('listem/index.html')
	c = Context({
   		'latest_lists_list': latest_lists_list,
   		})
	return HttpResponse(t.render(c))

def detail(request, lists_id):
    return HttpResponse("You're looking at list %s." % lists_id)

def fresh(request, lists_id):
    return HttpResponse("You're looking at a fresh new list %s." % lists_id)

# def vote(request, lists_id):
#     return HttpResponse("You're voting on lists %s." % lists_id)