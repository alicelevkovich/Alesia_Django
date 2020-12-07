from django.urls import path
from cw20.views import lines

urlpatterns = [
    path('lines/', lines, name='lines')
]
