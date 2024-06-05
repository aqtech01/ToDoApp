from django.shortcuts import render, redirect

from core.forms import ToDoForm
from core.models import ToDoItem


# Create your views here.
def home(request):
    data = ToDoItem.objects.all()
    context = {
        "data": data,
    }
    return render(request, "core/index.html", context)


def add_to_do(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            complete = form.cleaned_data["complete"]
            data = ToDoItem.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                complete=complete
            )
            return redirect("/home")  # Replace with your actual URL name or path
    else:
        form = ToDoForm()

    context = {
        "form": form,
        "title": "Add ToDo"
    }
    return render(request, "core/todo.html", context)
