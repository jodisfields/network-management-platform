from django.http import HttpResponse


def index(request):
    return HttpResponse("Fisso Network Visualisation.")
