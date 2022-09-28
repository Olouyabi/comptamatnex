from django.shortcuts import redirect, render
from vip.models import ViPost
from django.http import JsonResponse
from django.core import serializers
from compte.models import MembreUser


def membre_view(request):
    qs = ViPost.objects.all()
    member = MembreUser.objects.get(user=request.user)

    context = {
        'qs': qs,
        'navbar':'membre',
        'member' : member,
    }
    return render(request, 'membre.html', context)


def post_vip_json(request):
    qs = ViPost.objects.all()
    data = serializers.serialize('json', qs)
    return JsonResponse({'data':data})



    