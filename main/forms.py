from django import forms

from .models import ContactProfile


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Name',
                                   }))
                        
    email = forms.EmailField(
        max_length=100, required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Email',
                                   }))
    
    message = forms.CharField(
        max_length=100, required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Message',
                                   'rows': '6'
                                   }))
    
    
    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message')

    def save(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        contact = ContactProfile(name=name, email=email, message=message)
        contact.save()
        return contact
