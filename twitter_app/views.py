from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# Test
# Create your views here.
from twitter_app.forms import LoginForm, RegisterForm


def login_page_data():
    return {
        "login_form": LoginForm(),
        "register_form": RegisterForm(prefix="register"),
    }


# salam testsdadsakjdskjbjkda.j,ads.jn,a
def baseindexview(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    context = login_page_data()
    return render(request, "accounts/login.html", context)


def login_view(request):
    if request.method == "POST":
        context = login_page_data()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect("dashboard")
            else:
                context["message"] = "username or password invalid !"
                return render(request, "accounts/login.html", context)
        else:
            context["login_form"] = form
            return render(request, "accounts/login.html", context)
    else:
        return redirect("home")


def register_view(request):
    if request.method == "POST":
        context = login_page_data()
        form = RegisterForm(request.POST, prefix="register")
        if form.is_valid():
            full_name = form.cleaned_data.get("full_name")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.first_name = full_name.split()[0]
            user.last_name = full_name.split()[1]
            user.save()
            if user and user.is_active:
                login(request, user)
                return redirect("dashboard")
            else:
                context["message"] = "username or password invalid !"
                return render(request, "accounts/login.html", context)
        else:
            context["login_form"] = form
            return render(request, "accounts/login.html", context)
    else:
        return redirect("home")


# test2
def logout_view(request):
    logout(request)
    return redirect("home")


def dashboard_view(request):
    context = {}
    return render(request, "home/index.html", context)


def timeline_view(request):
    context = {}
    return render(request, "accounts/detail.html", context)
