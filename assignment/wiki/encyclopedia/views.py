from django.shortcuts import render

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
    