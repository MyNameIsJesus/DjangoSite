from django.shortcuts import render
from django.http import HttpResponse
data = {
    'title': "The site",
    "values": ["Hello", "Hi!", "Let's go", "That's the content of my site"],
    'heading': 'header',
    'text': 'the text'

}
def showpage(request):
    return render(request, "mainpage/main.html", data)

# Create your views here.
