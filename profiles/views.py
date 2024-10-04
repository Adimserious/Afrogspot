from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileDeleteForm
from .models import Profile
from checkout.models import Order


@login_required
def profile_view(request):
    try:
        # Check if profile exists
        profile = request.user.profile
        #profile, created = Profile.objects.get_or_create(user=request.user)
    except Profile.DoesNotExist:
        # Redirect to profile creation form if no profile exists
        messages.info(request, 'You do not have a profile. Please create one.')
        return redirect('create_profile')  # Adjust with the correct view name for creating a profile

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile information has been updated.')
            return redirect('profile_view')

    # Get user's order history
    orders = Order.objects.filter(user=request.user)

    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'user_name': request.user.get_full_name() or request.user.username
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def profile_delete(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST)
        if form.is_valid():
            profile.delete()
            messages.success(request, 'Your profile has been deleted.')
            return redirect('home')  # Redirect to home after deletion
    else:
        form = ProfileDeleteForm()

    return render(request, 'profiles/profile_delete_confirm.html', {'profile': profile, 'form': form})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Assign the user to the profile
            profile.save()
            messages.success(request, 'Your profile has been created.')
            return redirect('profile_view')

    else:
        form = ProfileForm()

    return render(request, 'profiles/create_profile.html', {'form': form})
