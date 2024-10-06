from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactMessageForm

@login_required
def send_message(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.user = request.user
            message.save()
            return redirect('contact_confirmation')
    else:
        form = ContactMessageForm()
    
    return render(request, 'contact/send_message.html', {'form': form})


@login_required
def list_user_messages(request):
    messages = ContactMessage.objects.filter(user=request.user)
    return render(request, 'contact/list_messages.html', {'messages': messages})


@login_required
def update_message(request, message_id):
    message = ContactMessage.objects.get(id=message_id, user=request.user)
    if request.method == 'POST':
        form = ContactMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('list_user_messages')
    else:
        form = ContactMessageForm(instance=message)
    
    return render(request, 'contact/update_message.html', {'form': form})


@login_required
def delete_message(request, message_id):
    message = ContactMessage.objects.get(id=message_id, user=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('list_user_messages')

    return render(request, 'contact/delete_message.html', {'message': message})


def contact_confirmation(request):
    return render(request, 'contact/contact_confirmation.html')
