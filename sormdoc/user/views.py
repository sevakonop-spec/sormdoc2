from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def profile(request):
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, instance=profile_obj)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('main:index')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile_obj)
    return render(request, 'user/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })