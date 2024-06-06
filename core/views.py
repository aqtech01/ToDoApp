from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from core.forms import ToDoForm
from core.models import ToDoItem


# Create your views here.
def home(request):
    data = ToDoItem.objects.all()
    context = {
        "data": data,
        "title": "Home"
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


def signup_view(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("signup")

        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "User successfully created")
            return redirect("signin")
        except Exception as e:
            messages.error(request, f"Something went wrong: {e}")

    return render(request, "auth/register.html", {"title": "Register"})


def signin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = authenticate(username=username, password=password)
            if user.is_authenticated:
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect("home")
            else:
                messages.error(request, "Username or password is incorrect")
        except Exception as e:
            messages.error(request, "Something went wrong {e}")
    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "logout Successfully")
    return redirect("signin")
