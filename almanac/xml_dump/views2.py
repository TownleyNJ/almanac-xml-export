from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from xml_dump.models import *
import re

def unit_tag(name, dictionary):
    text = "<"+name+" "
    for key in dictionary:
        text += key+'="'+dictionary[key]+'" '
    text += "/>"
    return text

def start_tag(name, dictionary):
    text = "<"+name+" "
    for key in dictionary:
        text += key+='="'+dictionary[key]+'" '
    text += ">"
    return text

def single_tag(tag_name, data):
    return "<"+tag_name+">"+data+"</"+tag_name+">"

def home(request, state):
    state = AapState.objects.get(postal=state)
    area = AapArea.objects.get(id=state.area_id)
    
    chapter_dict = {
        "id": state.postal,
        "state-name": area.name,
    }
    final = start_tag("chapter", chapter_dict)
    
    final += get_state_narrative(state)
    final += get_presidential_politics(state)
    final += get_congressional_districting(state)
    final += get_congressional_lineup(state, area)
    final += get_census(state, area)
    final += get_legislature(state, area)
    final += get_election_results(state, area)
    final += get_governor(state, area)
    final += get_senators(state, area)
    final += get_representatives(state, area)

    f = open("/home/nstein/Desktop/state_"+state.postal+".xml", "w")
    f.write(final)
    return final

def get_presidential_politics(state):
    return single_tag("presidential-politics", state.pres_politics)

def get_congressional_districting(state):
    return single_tag("congressional-districting", state.cong_districting)

def get_congressional_lineup(state, area):
    lineups = AapCongressionallineup.objects.filter(state_id=area.id)
    final = "<congressional-lineup>"
    for lineup in lineups:
        congress = AapCongress.objects.get(id=lineup.congress_id)
        
