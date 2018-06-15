from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import SignUpForm, ProfileForm,SignUpEditForm
from django.contrib import messages
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.models import Profile
from django.contrib.auth.views import login
from django.core.mail import send_mail
from django.conf import settings

#Eamil
subject = 'Account Created Successfully.'
message = 'Welcome To 24/7 Hunger Your ./n' \
          'Now You can order Food from any Restaurants./n' \
          'Just Visit the website and start Ordering.'


def SignUpView(request):
    template_name = 'accounts/index.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            email = form.cleaned_data['email']
            if email and User.objects.filter(email=email).exists():
                messages.success(request, "Email address"+" "+email+" "+"Already Registered.")
                return render(request, template_name, {'form': form})
            form1.save()
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, "Your account has been created Successfully")
            return redirect('accounts:profile')
        return render(request,template_name, {'form': form})
    else:
        form = SignUpForm
        return render(request, template_name, {'form': form})


@login_required
def ProfileView(request):
    template_name = 'accounts/Profile_form.html'

    if request.method == 'POST':
        form = SignUpEditForm(request.POST, instance=request.user)
        form1 = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid() and form1.is_valid():
            profile = form1.save(commit=False)
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            phone = form1.cleaned_data['phone']
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                messages.success(request, "Email address"+" "+email+" "+"Already Registered.")
                return render(request, template_name, {'form': form1, 'form1': form})

            elif phone and Profile.objects.filter(phone=phone).exclude(user=request.user).exists():
                messages.success(request, "Phone Number" + " " + phone + " " + "Already Registered.")
                return render(request, template_name, {'form': form1, 'form1': form})

            profile.save()
            user.save()
            messages.success(request, "Your Profile Updated Successfully.")
            return redirect('food:restaurants_list')
        return render(request, template_name, {'form': form1, 'form1': form})

    else:
        form = SignUpEditForm(instance=request.user or None)
        form1 = ProfileForm(instance=request.user.profile or None)
        context ={
            'form': form1,
            'form1': form
        }

        return render(request, template_name, context)



def copyright_policy(request):
    return render(request,'accounts/copyright.html', {})


def terms(request):
    return render(request, 'accounts/terms.html', {})


def privacy(request):
    return render(request, 'accounts/privacy.html', {})

