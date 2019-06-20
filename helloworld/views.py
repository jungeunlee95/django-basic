from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'helloworld/hello.html')

def hello2(request, id=0, user_id=''):
    return HttpResponse(f'id:{id}, user_id:{user_id}')