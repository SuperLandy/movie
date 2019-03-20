from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import urllib3,requests
from urllib import parse
urllib3.disable_warnings()

def home(request):
    return render(request, 'index.html')
def re_search(request):

    movie = request.GET.get('text')
    try:
        heimi_url = 'https://www.myxin.top/jx/api/'
        # 按照格式
        para = {
            'url':movie,
        }
        headers ={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Upgrade-Insecure-Requests':'1',
            'Connection':'keep-alive',
            'Host':'www.myxin.top',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        html = requests.get(heimi_url,params=para,headers=headers,verify=False)
        content = [html.url]
        return render(request, 're_search.html',{ 'content':content,'title':'点击即可观看'})
    except Exception as e:
        return HttpResponse(e)


def api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        movie = request.POST.get('url')
        if username =='sunjiajia' and password == 'biubiu':
            heimi_url = 'https://www.myxin.top/jx/api/'
            # 按照格式
            para = {
                'url': movie,
            }
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Upgrade-Insecure-Requests': '1',
                'Connection': 'keep-alive',
                'Host': 'www.myxin.top',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            }
            html = requests.get(heimi_url, params=para, headers=headers, verify=False)
            content = parse.unquote(html.url)

            code = {"msg":'OK',"url":content}
            return JsonResponse(code)
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')