from django import forms
from .models import Ideas

class PostForm(forms.ModelForm):

    class Meta:
        model = Ideas
        fields = ('date', 'costs', 'keyword')
