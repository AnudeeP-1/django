from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                widget=forms.TextInput(
                    attrs={'type':'text','class':'form-control', 'placeholder':'To do (enter here)', 'aria-label':'First name'}
                ))