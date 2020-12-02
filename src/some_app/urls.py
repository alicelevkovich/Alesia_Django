from django.urls import path
from some_app.views import index as ix, process_form, hello_user, render_name_form as rn, get_name


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('form', ix, name='ix'),
    path('process_form', process_form, name='process_form'),
    path('hello_user', hello_user),
    path('render_name_form', rn),
    path('get_name', get_name)
]
