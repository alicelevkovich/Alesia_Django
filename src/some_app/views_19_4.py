from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'some_app/form.html', {})


def process_form(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    comment = request.GET.get('comment')
    string_list = comment.split("\r\n")
    new_string = [element + f'(c) {name}' for element in string_list]
    result_string = "\r\n".join(new_string)
    return render(request, 'some_app/process_form.html', {'result_string': result_string})
