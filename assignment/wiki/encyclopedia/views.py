from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EntryForm
from . import util
import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def watch(request, title):
    return render(request, "encyclopedia/watch.html", {
        "title": title,
        "entry": markdown.markdown(util.get_entry(title))
    })

def create_entry(request):
    if request.method == 'POST':
    form = EntryForm(request.POST)
    if form.is_valid():
        "title": form.cleaned_data["title"]
        "content": form.cleaned_data["content"]
        return HttpResponseRedirect('/Looksvalid/')
    else:
        form = EntryForm()
        
    return render(request, "encyclopedia/create.html", {
        "form" : form
    })