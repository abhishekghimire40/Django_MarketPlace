from django import forms

from .models import ConversationMessages


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessages
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "w-full mt-2 h-20 py-4 px-6 rounded-xl border"}
            )
        }
