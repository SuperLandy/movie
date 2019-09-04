# Create your views here.

import requests
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.Analysis import analysis


def index(request):
    return render(request, 'index.html')


@login_required()
def movies(request):
    if request.method == 'GET':
        return render(request, 'moves_search.html')

    if request.method == 'POST':
        passageway = request.POST.get('passageway', None)
        movie_url = request.POST.get('movie_url', None)
        if passageway == '1':
            ki_host = 'https://www.9ki.cc/jx.php'
            result = analysis(host=ki_host, movie=movie_url)
            if result['code'] == '0000':
                return JsonResponse({'code': '0000', 'result': result['msg']})
            else:
                return JsonResponse({'code': '8999', 'result': '解析通道失败，请切换其他通道'})

        elif passageway == '2':
            gxj_host = 'http://jx.drgxj.com'
            result = analysis(host=gxj_host, movie=movie_url)
            if result['code'] == '0000':
                return JsonResponse({'code': '0000', 'result': result['msg']})
            else:
                return JsonResponse({'code': '8999', 'result': '解析通道失败，请切换其他通道'})

        elif passageway == '3':
            ge_host = 'http://jx.618ge.com/jx/3.php'
            result = analysis(host=ge_host, movie=movie_url)
            if result['code'] == '0000':
                return JsonResponse({'code': '0000', 'result': result['msg']})
            else:
                return JsonResponse({'code': '8999', 'result': '解析通道失败，请切换其他通道'})

        elif passageway == '4':
            vip_host = 'http://vip.jlsprh.com/'
            result = analysis(host=vip_host, movie=movie_url)
            if result['code'] == '0000':
                return JsonResponse({'code': '0000', 'result': result['msg']})
            else:
                return JsonResponse({'code': '8999', 'result': '解析通道失败，请切换其他通道'})