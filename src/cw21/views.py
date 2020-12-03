from django.shortcuts import render
from cw21.form import CreateStudent
from cw21.models import Student


def home(request):

    if request.method == 'GET':
        # some_context = {
        #     'name': 'Alesia'
        # }
        students_list = Student.objects.all()
        context = {'students': students_list}
        return render(request, 'home_page.html', context=context)
    # elif request.method == 'POST':
    #     return render(request, 'home_page.html', context={})


def create_student(request):
    context = {
        'form': CreateStudent(),
    }
    if request.method == 'GET':
        return render(request, 'create_student.html', context=context)

    elif request.method == 'POST':
        student = Student.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            age=request.POST.get('age'),
            profession=request.POST.get('profession')
        )
        return render(request, 'home_page.html')

