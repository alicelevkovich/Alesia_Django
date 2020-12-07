from django import forms


class WriteLinesForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0, max_value=100)
    comment = forms.CharField(max_length=200)


class DeleteLinesForm(forms.Form):
    # confirmation = forms.CheckboxInput()
    _method = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'DELETE'}))
