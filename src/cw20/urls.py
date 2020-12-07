from django.urls import path
from cw20.views import lines, delete_lines

urlpatterns = [
    path('lines/', lines, name='lines'),
    path('delete_lines/', delete_lines, name='delete_lines')
]
