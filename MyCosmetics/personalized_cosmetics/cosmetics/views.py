from django.shortcuts import render
from .forms import CosmeticPreferenceForm

def home(request):
    if request.method == 'POST':
        form = CosmeticPreferenceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'cosmetics/result.html', {'data': data})
    else:
        form = CosmeticPreferenceForm()
    return render(request, 'cosmetics/home.html', {'form': form})

def page1(request):
    return render(request, 'cosmetics/page1.html')

def personalize(request):
    return render(request, 'cosmetics/personalize.html')

def result(request):
    # This view is already handled by the `home` view when the form is submitted.
    return render(request, 'cosmetics/result.html')

def about(request):
    return render(request, 'cosmetics/about.html')

def tips(request):
    return render(request, 'cosmetics/tips.html')

def blank(request):
    return render(request, 'cosmetics/blank.html')