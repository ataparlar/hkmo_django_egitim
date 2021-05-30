from django.shortcuts import render
from .models import *


# Create your views here.

def board_view(request):
    year = 2020
    boardMembers = BoardMember.objects.all()
    advisors = Advisor.objects.all()
    board_dict = {
        "boardMembers": boardMembers,
        "advisors": advisors
    }
    return render(request, 'board.html', board_dict)


