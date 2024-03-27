from django.shortcuts import get_object_or_404, render

from .models import teams

# Create your views here.
def index(request):
    ordered_teams = teams.objects.order_by("-points")
    context = {"ordered_teams": ordered_teams}
    return render(request, "scores/index.html", context)
    
def detail(request, team_id):
    team = get_object_or_404(teams, pk=team_id)
    return render(request, "scores\detail.html", {"team": team})
