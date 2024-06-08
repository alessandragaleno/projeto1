from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    text = forms.TextField(widget=forms.Textarea)
    email = forms.EmailField()
    copie = forms.BooleanField(required=False)