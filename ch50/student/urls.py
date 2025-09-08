from django.urls import path
from student.views import home, course, result
from django.views.decorators.cache import cache_page

urlpatterns = [
    # HERE see that home page  can run three urls so we 
    # can store caching of each urls 
    path('', home, name="home"),
    path('home/', cache_page(30)(home), name="home1"),
    path('index/', home, name="index"),

    path('course/', course, name="course"),
    path('result/', cache_page(30)(result), name="result"),
]
