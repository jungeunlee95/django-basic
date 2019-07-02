from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')

def hello2(request, id=0, user_id=''):
    return HttpResponse(f'id:{id}, user_id:{user_id}')

def hello3(request):
    jsonresult = {
        'result' : 'success',
        'data' : ['hello', 1, 2, True, ('a','b','c')]
    }

    return JsonResponse(jsonresult)

def counter_add(reqeust):
    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()

    return HttpResponse(f'ok! add')

def counter_update(request):
    # django query set 검색해보기
    # 그룹넘 = 1, 오더넘 >= 2 의 게시물의
    # 오더넘 +1 씩 증가
    # __gt, __lt, __gte, __lte : 비교조건
    Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno')+1)
                                                            # F('orderno')객체 = 현재 orderno값


    return HttpResponse(f'ok! update')

def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))

    return HttpResponse(f'max groupno : {value["max_groupno"]}')