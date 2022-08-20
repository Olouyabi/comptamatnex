from django.shortcuts import redirect, render
from vip.models import ViPost


def membre_view(request):
    qs = ViPost.objects.all()
    context = {
        'qs': qs,
        'navbar':'membre',
    }
    return render(request, 'membre.html', context)

