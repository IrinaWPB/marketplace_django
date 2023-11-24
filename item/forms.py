
from django import forms
from .models import Item

INPUT_STYLES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ('category', 'name', 'description', 'price', 'image')
    widgets = {
      'category': forms.Select(attrs={
        'class':INPUT_STYLES
      }),
      'name': forms.TextInput(attrs={
        'class':INPUT_STYLES
      }),
      'description': forms.Textarea(attrs={
        'class':INPUT_STYLES
      }),
      'price': forms.TextInput(attrs={
        'class':INPUT_STYLES
      }),
      'image': forms.FileInput(attrs={
        'class':INPUT_STYLES
      })
    }

class EditItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ('name', 'description', 'price', 'image', 'is_sold')
    widgets = {
      'name': forms.TextInput(attrs={
        'class':INPUT_STYLES
      }),
      'description': forms.Textarea(attrs={
        'class':INPUT_STYLES
      }),
      'price': forms.TextInput(attrs={
        'class':INPUT_STYLES
      }),
      'image': forms.FileInput(attrs={
        'class':INPUT_STYLES
      })
    }
  