from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm,UserUpdationForm,UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            ## Flash Messages ##
            # message.debug
            # message.warning
            # message.success
            # message.error
            # message.info
            messages.success(request,f'Your account has been created successfully created!!, You can login now!')
            return redirect('user-login')

    else:
        form = UserRegistrationForm()
    return render(request,"users/register.html",{'form':form})

@login_required
def profile(request):
    if request.method=="POST":
        u_form = UserUpdationForm(request.POST,instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('user-profile')
    else:
        u_form = UserUpdationForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)
    context={
    "u_form":u_form,
    "p_form":p_form
    }
    return render(request,"users/profile.html",context)
