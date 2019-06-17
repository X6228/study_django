from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return HttpResponse("hello_world")

def current_time(request):
    now = datetime.datetime.now()
    html = f"It is now {now}."
    return HttpResponse(html)

def ahead_hours(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = f'in {offset} hour(s),it will be {dt}.'
    return HttpResponse(html)