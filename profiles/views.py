from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from checkout.models import Order

@login_required
def profile_view(request):
    # Checks if the profile exists; if not, create one
    profile, created = Profile.objects.get_or_create(user=request.user)

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile information has been updated.')
            return redirect('profile_view')  # Redirect to the profile page after saving

    # Get user's order history
    orders = Order.objects.filter(user=request.user)

    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'profiles/profile.html', context)