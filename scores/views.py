from django.shortcuts import get_object_or_404, render
from .models import teams, ports

# Create your views here.
def index(request):
    ordered_teams = teams.objects.order_by("-points")
    context = {"ordered_teams": ordered_teams}
    return render(request, "scores/index.html", context)
    # Now I need to display the information from this query:
    # select * from targets natural join ports
    # where team_id = 1 -- this value can be a variable and I can do this for each team :D
    
def detail(request, team_id):
    team = get_object_or_404(teams, pk=team_id) # get team object given team_id
    ports_for_team = ports.objects.filter(target__team_id=team_id).order_by("-points_obtained") # order ports from given team by points
    context = {"team": team, "ports": ports_for_team}
    return render(request, "scores\detail.html", context)
