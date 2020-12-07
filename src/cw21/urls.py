from django.urls import path
from cw21.views import home, create_student

urlpatterns = [
    path('home', home, name='page'),
    path('add/', create_student, name='student')

]
