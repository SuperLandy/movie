# Create your views here.


from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def accounts_login(request):
    method = request.method
    if method == 'GET':
        return render(request, 'index.html')
    if method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            auth = authenticate(username=username, password=password)
            if auth is None:
                return JsonResponse({'code': '9998', 'msg': 'USERNAME OR PASSWORD ERROR!',
                                     'result': {'user info is': username}}
                                    )
            elif auth.is_active is False:
                return JsonResponse({'code': '9997', 'msg': 'USERNAME IS DISABLE!',
                                     'result': username + '已禁用'})
            else:
                login(request, user=auth)
                request.session['is_superuser'] = auth.is_superuser
                request.session['username'] = auth.username
                return JsonResponse({'code': '0000', 'msg': 'login success'})
        else:
            return JsonResponse({'code': '9996', 'msg': 'ARGS ERROR'})
    else:
        return JsonResponse({'code': '9995', 'msg': 'METHOD ERROR'})

