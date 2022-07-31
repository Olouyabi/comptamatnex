from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render
from contact.models import Contact



# Create your views here.
def contact_view(request):

    context = {
        'navbar':'contact',
    }
    return render(request, 'pages/contact.html', context)
