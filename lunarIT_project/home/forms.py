from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
    
