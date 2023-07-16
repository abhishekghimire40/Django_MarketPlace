from django import forms

from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "name",
            "description",
            "price",
            "image",
            "category",
        )
        # another way to style our form. if done this way it should be inside meta class
        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "image", "is_sold")

        # styling our form
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
