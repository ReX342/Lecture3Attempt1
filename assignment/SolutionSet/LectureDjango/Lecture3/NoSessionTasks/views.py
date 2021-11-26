from django.shortcuts import render

tasks = [ "fe", "da", "ds"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })