from django.shortcuts import render
from django.http import JsonResponse
from hltv.parsers.event_parser import EventParser


def get_players(request):
    players = list()

    event = EventParser(5469)
    for player in event.get_event_players():
        data = {'code': player[0], 'href': player[1], 'nickname': player[2]}
        players.append(data)

    return JsonResponse(players, safe=False)

