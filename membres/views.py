from django.shortcuts import redirect, render
from membres.models import MembresComptaMatNex


def membre_view(request):
    return render(request, 'membre.html', {'navbar':'membre',})

