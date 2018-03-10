from django import forms
from . import models


class PollForm(forms.ModelForm):
    class Meta:
        model = models.Choice
        fields = ('question', 'choice_text', )
