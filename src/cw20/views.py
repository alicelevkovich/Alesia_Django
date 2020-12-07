from django.http import HttpResponse
from django.shortcuts import render
from cw20.forms import WriteLinesForm, DeleteLinesForm


def lines(request):
    context = {
        'form': WriteLinesForm(),
        'delete_form': DeleteLinesForm()
    }
    if request.method == 'GET':

        return render(request, 'write_lines_form.html', context=context)

    elif request.method == 'POST':
        form = WriteLinesForm(request.POST)
        if not form.is_valid():
            errors = form.errors
            return HttpResponse(f'Errors {errors}')

        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        age = data.get('age')
        context['first_name'] = first_name
        context['last_name'] = last_name
        context['age'] = age
        with open('person_data', 'a') as person_data_file:
            person_data_file.write(f'{first_name} {last_name} {age}\n')
        return render(request, 'view_page.html', context=context)

    elif request.method == 'DELETE':
        return HttpResponse(f'yo')








