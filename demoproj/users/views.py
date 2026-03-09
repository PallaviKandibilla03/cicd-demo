from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            messages.success(request, f'Account has been successfully created for {un}!')
            return redirect('sign_in')
    else:  # GET request
        form = UserSignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})