from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    