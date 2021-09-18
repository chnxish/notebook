from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hello(request):
    if request.method == 'GET':
        return JsonResponse({'name': 'Xish'}, safe=False)
