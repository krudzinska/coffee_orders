from django.shortcuts import render
from .models import Provider
from django.shortcuts import render, get_object_or_404
from .forms import ProviderForm
from django.shortcuts import redirect

def providers_list(request):
    providers = Provider.objects.order_by('name')
    return render(request, 'coffeeshop/providers_list.html', {'providers' : providers})

def provider_detail(request, pk):
    provider = get_object_or_404(Provider, pk=pk)
    return render(request, 'coffeeshop/provider_detail.html', {'provider': provider})

def offer_list(request):
    providers = Provider.objects.order_by('name')
    return render(request, 'coffeeshop/offer_list.html', {'providers' : providers})

def provider_new(request):
    form = ProviderForm()
    return render(request, 'coffeeshop/provider_edit.html', {'form': form})

def provider_new(request):
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.save()
            return redirect('provider_detail', pk=provider.pk)
    else:
        form = ProviderForm()
    return render(request, 'coffeeshop/provider_edit.html', {'form': form})

def login(request):
    return render(request, 'coffeeshop/login.html', {})

