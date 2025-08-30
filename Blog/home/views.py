from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm

def home(request):
    posts = Post.objects.all()
    return render(request, "home/home.html", {"posts":posts})
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            # Створюємо користувача
            User.objects.create(
                username=username,
                email=email,
                password=make_password(password)  # хешуємо пароль!
            )
            return redirect("home")  # після реєстрації перенаправляємо
    else:
        form = RegisterForm()

    return render(request, "home/register.html", {"form": form})