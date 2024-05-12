from django import forms

from .models import Message

CLASS_NEW = 'w-full py-4 px-6 rounded-xl'

class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Message...',
        'class': CLASS_NEW,
    }))

    class Meta:
        model = Message
        fields = ["message",]
