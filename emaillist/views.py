from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    emaillist = Emaillist.objects.all().order_by('-id')
    # for email in emaillist:
    #     print(email)
    data = {'emaillist':emaillist}
    return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')

def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']
    emaillist.save()

    # insert 후에는 꼭 redirect 처리!
    return HttpResponseRedirect('/emaillist')