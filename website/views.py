from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    template_path = 'website/index.html'
    context = {}
    context["username"] = "12C"
    context["last_name"] = "aaa"

    return render(request, template_path, context)
