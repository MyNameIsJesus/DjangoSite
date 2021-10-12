from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class Articleform (ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'announce', 'full_text', 'date']

        widgets = {"title": TextInput(attrs={"class": 'form-control', "placeholder": "Title"}),
                   "announce": TextInput(attrs={"class": 'form-control', "placeholder":"Announce"}),
                   "full_text": Textarea(attrs={"class": "form-control", "placeholder": "Text of an article"}),
                   "date": DateTimeInput(attrs={"class": "form-control"})

                   }
