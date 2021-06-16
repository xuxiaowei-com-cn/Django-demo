import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request):
    data = {}
    if request.method == 'GET':
        data['code'] = 0
        data['msg'] = '成功'
        response = HttpResponse(json.dumps(data, ensure_ascii=False))
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        data['msg'] = 1
        data['msg'] = '失败'
        response = HttpResponse(json.dumps(data, ensure_ascii=False))
        response.headers['Content-Type'] = 'application/json'
        return response
