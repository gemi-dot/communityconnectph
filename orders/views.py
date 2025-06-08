
# Create your views here.
from django.shortcuts import render, redirect
from .forms import WaterRefillRequestForm

def water_order_request(request):
    if request.method == 'POST':
        form = WaterRefillRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'orders/thank_you.html')
    else:
        form = WaterRefillRequestForm()
    return render(request, 'orders/water_order_form.html', {'form': form})
