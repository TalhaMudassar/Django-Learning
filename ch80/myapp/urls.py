from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.AllStudentView.as_view(), name='all_student'),
    path('students/',views.StudentListView.as_view(),name='students'),
    path('students1/',views.StudentListView1.as_view(),name='students1'),
    path('students2/',views.StudentListView2.as_view(),name='students2'),
    path('students3/',views.StudentListView3.as_view(),name='students3'),
    # path('students/', views.StudentListView.as_view(), name='students'),
    # path('students1/', views.StudentListView1.as_view(), name='students1'),
    # path('students2/', views.StudentListView2.as_view(), name='students2'),
    # path('students3/', views.StudentListView3.as_view(), name='students3'),
]
