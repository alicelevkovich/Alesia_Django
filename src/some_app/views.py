from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, 'form.html', {})


def process_form(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    comment = request.POST.get('comment')
    string_list = comment.split("\r\n")
    new_string = [element + f'(c) {name}' for element in string_list]
    result_string = "\r\n".join(new_string)
    return render(request, 'process_form.html', {'result_string': result_string})


def hello_user(request):
    template = loader.get_template('hello_user.html')
    context = {'name': request.GET.get('name')}
    return HttpResponse(template.render(context, request))


def render_name_form(request):
    return render(request, 'name_form.html')


def get_name(request):
    name = request.POST.get('name')
    context = {'name': request.POST.get('name')}
    return render(request, 'process_name_form.html', context)


