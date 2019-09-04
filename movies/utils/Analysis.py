from requests import get
import requests

requests.packages.urllib3.disable_warnings()


def analysis(host, movie):
    try:
        para = {'url': movie}
        html = get(host, params=para, verify=False)
        content = [html.url]
        return {'code': '0000', 'msg': content}
    except Exception as error:
        return {'code': '8999', 'msg': error}
