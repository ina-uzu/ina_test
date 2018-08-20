from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from main.models import Speed


def show_main(request):
    return render(request, 'main/main.html')


def add_speed(request):
    if 'speed' not in request.POST:
        return HttpResponse('속도를 입력해주세요')
    else:
        if len(request.POST['speed']) == 0:
            return HttpResponse('속도를 입력해주세요')
        else:
            entry_speed = request.POST['speed']

    new_speed = Speed(speed=entry_speed)

    try:
        new_speed.save()

    except:
        return HttpResponse('입력이 실패하였습니다')

    return HttpResponse('모터 스피드 ' + entry_speed + '입력')
