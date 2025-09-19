from django.urls import path
from myapp import views

urlpatterns = [
    path('fun1/',views.myfunview1,name='myfunview1'),
    path('fun2/',views.myfunview2,name='myfunview2'),
    path('homefun/',views.homefunview,name='home_fun_view'),
    path('aboutfun/',views.aboutfunview,name='aboutfunview'),
    # #first  1.view that we define in views.py
    # path('newsfun/',views.newsfunview,name='newsfun'),
    #second 2.view that we define in views.py
    path('newsfun/',views.newsfunview,{'template_name':'myapp/news.html'},name='newsfun'),
    path('newsfun2/',views.newsfunview,{'template_name':'myapp/news2.html'},name='news_fun2_view'),
    path('contactfun/',views.contactfunview,name='contact_fun_view'), 
    
    
    
    #class based view:
    path('cl1/',views.MyClassView1.as_view(),name='classview1'),
    path('cl2/',views.MyClassView2.as_view(),name='classview2'),
    path('cl3/',views.MyClassView3.as_view(),name='classview3'),
    # path('cl3/',views.MyClassView3.as_view(data='here the data pass through url '),name='classview3'),
    # inheritance:
    path('childcl3/',views.MyChildClassView3.as_view(),name='classview3'),
    path('homefun/',views.HomeClassView.as_view(),name='home_fun_view'),
    path('aboutfun/',views.AboutClassView.as_view(),name='about_fun_view'),
    path('newsfuncbb/',views.NewsClassView.as_view(template_name='myapp/news.html'),name='newsfunn'),
    path('newsfuncbb2/',views.NewsClassView.as_view(template_name='myapp/news2.html'),name='newsfunn'),
    path('contactfunc1/',views.ContactClassView.as_view(),name='contact_fun_vieww'), 
    
    
    
]
