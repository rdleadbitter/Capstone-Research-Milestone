from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello from Django!</h1>")