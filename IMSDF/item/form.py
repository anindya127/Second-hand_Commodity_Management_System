from django import forms

from .models import Item

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASS_SMALL = 'w-auto py-3 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name', 'description', 'quantity','price', 'image', 'is_old', 'is_sold']
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS_SMALL}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASS_SMALL}),
            'quantity': forms.NumberInput(attrs={'class': INPUT_CLASS_SMALL}),
            'is_old': forms.CheckboxInput(attrs={'class': INPUT_CLASS}),
            'is_sold': forms.CheckboxInput(attrs={'class': INPUT_CLASS}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name', 'description', 'quantity','price', 'image', 'is_old', 'is_sold']
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS_SMALL}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASS_SMALL}),
            'quantity': forms.NumberInput(attrs={'class': INPUT_CLASS_SMALL}),
            'is_old': forms.CheckboxInput(attrs={'class': INPUT_CLASS}),
            'is_sold': forms.CheckboxInput(attrs={'class': INPUT_CLASS}),
        }
        
