from django.shortcuts import render, redirect
from .models import Subscriber
from .forms import SubscriberForm
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not Subscriber.objects.filter(email=email).exists():
                form.save()
                messages.success(request, 'Thank you for subscribing!')
            else:
                messages.info(request, 'You are already subscribed.')
            return redirect('subscribe')
    else:
        form = SubscriberForm()
    subscribers = Subscriber.objects.all().order_by('-subscribed_on')
    return render(request, 'newsletter/subscribe.html', {'form': form, 'subscribers': subscribers})
