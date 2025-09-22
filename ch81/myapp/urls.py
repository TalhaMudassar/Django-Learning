from django.urls import path
from myapp import views

urlpatterns = [
    path('<int:pk>/', views.SingleStudentView.as_view(),name='single_stuents'),
    path('student/<int:pk>',views.StudentDetailView.as_view(),name='student_detail'),
    path('student1/<int:geek>',views.StudentDetailView1.as_view(),name='student_detail1'),
    path('student2/<int:geek>',views.StudentDetailView2.as_view(),name='student_detail2'),
    path('student3/<int:geek>',views.StudentDetailView3.as_view(),name='student_detail3'),
    path('student4/<int:pk>',views.StudentDetailView4.as_view(),name='student_detail4'),
    path('student5/<int:pk>',views.StudentDetailView5.as_view(),name='student_detail5'),
]

