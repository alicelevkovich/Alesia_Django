from django.http import HttpResponse


def index(request):
    name = request.GET.get('name')
    lastname = request.GET.get('lastname')
    age = request.GET.get('age')

    if not age or age and int(age) < 18:
        return HttpResponse(f'Permission Denied')

    return HttpResponse(f'Welcome {name} {lastname}!')


