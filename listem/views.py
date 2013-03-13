from listem.models import Lists
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	latest_lists_list = Lists.objects.all()
	return render_to_response('listem/index.html', {'latest_lists_list': latest_lists_list}, context_instance=RequestContext(request))


def login_user(request):
	message = "FoodStar"
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/index')
			else:
				message = "You're account is not active, please contact the site."
		else:
			message = "Try Again."
	return render_to_response('listem/login.html', {"message":message}, context_instance=RequestContext(request))

def logout_user(request):
	logout(request)
	return HttpResponse("You are successfully logged out.")

@login_required
def my_lists(request):
	latest_lists_list = Lists.objects.all()
	return render_to_response('listem/my_lists.html', {'latest_lists_list': latest_lists_list})

@login_required
def create_lists(request):

    #return HttpResponse("You're looking at a fresh new list %s." % lists_id)
    return HttpResponse("Create new lists!")
