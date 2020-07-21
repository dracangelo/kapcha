from django import forms
from .models import Reserve

class ContactForm(forms.Form):
    subject = forms.CharField()
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = '__all__'