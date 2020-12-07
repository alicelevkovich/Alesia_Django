from django import forms


class CreateStudent(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0, max_value=100)
    profession = forms.CharField(max_length=200)
