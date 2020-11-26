from django.urls import path
from some_app.views_19_4 import index as ix, process_form


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('form', ix, name='ix'),
    path('process_form', process_form, name='process_form')
]
