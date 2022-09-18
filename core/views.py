from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    error = None
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            form = form.cleaned_data
            username = form.get("username")
            password = form.get("password")
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect("movies:home")

        else:
            error = "Error"

    context = {
        "form": form,
        "error": error
    }

    return render(request, "auth/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")