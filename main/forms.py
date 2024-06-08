from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    copie = forms.BooleanField(required=False)

class TodoForm(forms.Form):
    todo = forms.CharField(max_length=100)

class ItemForm(forms.Form):
    item = forms.CharField(max_length=100)