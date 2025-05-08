from django.shortcuts import render
from .forms import CandidatForm

def inscription_view(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'inscription/success.html')
    else:
        form = CandidatForm()
    return render(request, 'inscription/form.html', {'form': form})


def accueil(request):
    return render(request, 'inscription/accueil.html')