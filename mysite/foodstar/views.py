from django.template import Context, loader
from foodstar.models import foodlist
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the foodstar index")

def detail(request, foodlist_id):
	return HttpResponse("You are at the details of the list %s" %foodlist_id)

def fresh(request, foodlist_id):
	return HttpResponse("You are looking at a fresh list")

#def 