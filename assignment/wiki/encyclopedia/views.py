from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse


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
            title  = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            render(request, "encyclopedia/create.html", {
        "form" : form
        })
        else:
            #reload form with its fields
            form = EntryForm()
    else:
        # GET: click Create New Page in navbar: Get a new form (with fields)
        form = EntryForm()
       
    return render(request, "encyclopedia/create.html", {
        "form" : form
    })
    
def random(request):
    render(request, "encyclopedia/random.html")