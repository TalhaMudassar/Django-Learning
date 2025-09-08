from django.urls import path
from course.views import learn_djagno,learn_fastapi
urlpatterns = [
    path('learning1/',learn_djagno,name="learn_djagno"),
    path('learning2/',learn_fastapi,name="learn_fastapi"),
]
