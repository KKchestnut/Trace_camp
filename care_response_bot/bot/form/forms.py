from django import forms
from bot.models import BotResponse


class BotResponseForm(forms.ModelForm):
    class Meta:
        model = BotResponse

        fields = ['name', 'responses']
