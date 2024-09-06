from django.shortcuts import render


# Create your views here.
def home(request, **kwargs):
    template_name = 'core/home.html'
    context = dict()
    return render(request, template_name, context)
