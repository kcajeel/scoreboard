from django.shortcuts import render
from django.http import HttpResponse
from scores.models import teams

# Create your views here.
def home(request):
    ordered_teams = teams.objects.order_by("-points")
    output = ", ".join([(t.name + ', ' + str(t.points)) for t in ordered_teams])
    return HttpResponse(output)