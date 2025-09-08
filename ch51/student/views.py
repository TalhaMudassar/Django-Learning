from django.shortcuts import render
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.http import HttpResponse

def course(request):
  return render(request, 'student/course.html')


def clear_cache(request):
    cache.clear()   # deletes ALL cached fragments
    return HttpResponse("All cache cleared successfully!")


def clear_sidebar_cache(request):
    key = make_template_fragment_key("sidebar")  # same name you used in {% cache %}
    cache.delete(key)
    return HttpResponse("Sidebar cache cleared successfully!")

