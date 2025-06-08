from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import WaterRefillRequest, WaterStation
from django import forms

# Inline form for staff assignment and status update
class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = WaterRefillRequest
        fields = ['assigned_station', 'status']

@staff_member_required
def staff_dashboard(request):
    requests = WaterRefillRequest.objects.all().order_by('-id')
    return render(request, 'orders/staff_dashboard.html', {'requests': requests})

@staff_member_required
def update_request(request, pk):
    refill_request = get_object_or_404(WaterRefillRequest, pk=pk)
    if request.method == 'POST':
        form = StaffUpdateForm(request.POST, instance=refill_request)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = StaffUpdateForm(instance=refill_request)
    return render(request, 'orders/update_request.html', {'form': form, 'refill_request': refill_request})
