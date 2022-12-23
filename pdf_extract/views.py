from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from .utils import  text_extract

@login_required(login_url="login")
def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            initial_obj = form.save(commit=False)
            initial_obj.save()
            text = text_extract(initial_obj.document.path)
            extraction = ExtractedText(user=request.user,\
                 extract=text, document=initial_obj)
            extraction.save()
            return redirect('extracted_text_detail', id=extraction.id)
    else:
        form = DocumentForm()
    return render(request, 'pdf_extract/index.html', {
        'form': form
    })

@login_required(login_url="login")
def extracted_text_list(request):
    extracts = ExtractedText.objects.all().filter(user=request.user).order_by('-document__uploaded_at')
    return render(request, 'pdf_extract/extracted_text_list.html',{
        'extracts':extracts
    })

@login_required(login_url="login")
def extracted_text_detail(request, id):
    extract = get_object_or_404(ExtractedText, pk=id)
    return render(request, 'pdf_extract/extracted_text_detail.html',{
        'extract':extract
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pdf_extract/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "pdf_extract/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "pdf_extract/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "pdf_extract/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pdf_extract/register.html")

