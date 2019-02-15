from django.http import JsonResponse, HttpResponse

# Create your views here.
from course.task import CourseTask


def do(request):
    print('start do request')
    CourseTask.delay()
    print('end do request')
    # return JsonResponse({'result': 'ok'})
    return HttpResponse()
