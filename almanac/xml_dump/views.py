from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from xml_dump.models import *
from xml.sax.saxutils import escape
import re
import shutil
import os
import xml.etree.ElementTree as ET
import urllib

# -*- coding: utf-8 -*-

def check_states(request):
    state_array = [
        'AL',
        'AK',
        'AZ',
        'AR',
        'CA',
        'CO',
        'CT',
        'DE',
        'FL',
        'GA',
        'HI',
        'ID',
        'IL',
        'IN',
        'IA',
        'KS',
        'KY',
        'LA',
        'ME',
        'MD',
        'MA',
        'MI',
        'MN',
        'MS',
        'MO',
        'MT',
        'NE',
        'NV',
        'NH',
        'NJ',
        'NM',
        'NY',
        'NC',
        'ND',
        'OH',
        'OK',
        'OR',
        'PA',
        'RI',
        'SC',
        'SD',
        'TN',
        'TX',
        'UT',
        'VT',
        'VA',
        'WA',
        'WV',
        'WI',
        'WY']
    
    #state_array = ['MT']
    for state in state_array:
        base = "/home/nstein/Desktop/Export/"
        #Making State Directory
        os.makedirs(base+state)
        #Making Photos Directory
        os.makedirs(base+state+"/Photos")
        os.makedirs(base+state+"/Photos/GOV")
        os.makedirs(base+state+"/Photos/House")
        os.makedirs(base+state+"/Photos/Sen")
        #Placing file
        test = state_export(state, base+state+"/"+state+".xml")
        if test:
            print("Successfully created file for "+state)
        #Get Governor Photo
        state_object = AapState.objects.get(postal=state)
        area = AapArea.objects.get(id=state_object.area_id)
        seat = AapSeat.objects.filter(area_id=area.id).get(seattype='gov')
        tenure = AapTenure.objects.filter(seat_id=seat.id).order_by("-termexpires")[0]
        person = AapPerson.objects.get(id=tenure.person_id)
        try:
            photo = AapPhoto.objects.get(person_id=person.id)
            photo_version = AapPhotoversion.objects.filter(photo_id=photo.id).get(scheme='profile')
            photo_url = "http://www.nationaljournal.com/static/"
            photo_url += photo_version.file
            photo_name = person.last_name+"_"+state+"_GOV"
            urllib.urlretrieve(photo_url, base+state+"/Photos/GOV/"+photo_name)
        except:
            True

        #Get Senator Photos
        senate_seats = AapSeat.objects.filter(seattype='sen').filter(area_id=area.id)
        for seat in senate_seats:
            tenure = AapTenure.objects.filter(seat_id=seat.id).order_by("-start_date")[0]
            person = AapPerson.objects.get(id=tenure.person_id)
            a_person = person.id
            photo = AapPhoto.objects.filter(person_id=person.id)[0]
            a_photo_version = photo.id
            photo_version = AapPhotoversion.objects.filter(photo_id=photo.id).filter(scheme='profile')[0]
            photo_url = "http://www.nationaljournal.com/static/"
            photo_url += photo_version.file
            photo_name = person.last_name+"_"+state
            if seat.seatrank == "sr":
                photo_name += "_SRSEN"
            else:
                photo_name += "_JRSEN"
            urllib.urlretrieve(photo_url, base+state+"/Photos/Sen/"+photo_name)
        
        #Get House Photos
        district_area_ids = AapDistrict.objects.filter(state_id=state_object.area_id).values("area_id")
        house_seats = AapSeat.objects.filter(area_id__=district_area_ids)
        for seat in house_seats:
            tenure = AapTenure.objects.filter(seat_id=seat.id).order_by("-start_date")
            if tenure:
                tenure = tenure[0]
            else:
                continue
            
            person = AapPerson.objects.get(id=tenure.person_id)
            a_person = person.id
            photo = AapPhoto.objects.filter(person_id=person.id)[0]
            a_photo_version = photo.id
            photo_version = AapPhotoversion.objects.filter(photo_id=photo.id).filter(scheme='profile')[0]
            photo_url = "http://www.nationaljournal.com/static/"
            photo_url += photo_version.file
            photo_name = person.last_name+"_"
            photo_name += state+"_"
            photo_name += "DIST"
            district = AapDistrict.objects.get(area_id=seat.area_id)
            if district.number < 10:
                photo_name += "0"
            photo_name += str(district.number)
            urllib.urlretrieve(photo_url, base+state+"/Photos/House/"+photo_name)
            
        

        document = ET.parse(base+state+"/"+state+".xml")
        root = document.getroot()
    return HttpResponse("Done")    

def home(request, state):
    state_data = state_export(state)
    return HttpResponse(state_data)



def state_export(state, filepath):
    state_object = AapState.objects.get(postal=state)
    area_object = AapArea.objects.get(id=state_object.area_id)
    #Runs all collaborative functions to generate relevant parts of the XML
    #Compiles them into the final variable for display    
    final = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>'
    final += "<chapter "+tag_set("id", state)+tag_set("state-name", area_object.name)+'>\n<state>'
    final += get_state_narrative_tag(state)
    final += get_presidential_politics(state)
    final += get_congressional_districting(state)
    final += get_congressional_lineup(state)
    final += get_census(state)
    final += get_legislature(state)
    final += get_election_results(state)
    final += get_governor(state)
    final += get_senators(state)
    final += get_representatives(state)
    final += "</state></chapter>"

#Un-escape quotesi
    final = final.replace("&rdquo;",'&quot;')
    final = final.replace("&ldquo;",'&quot;')
    final = final.replace("&rsquo;","'")
    final = final.replace("&lsquo;","'")
    final = final.replace("&mdash;","-")
    final = final.replace("&ndash;", "-")
    final = final.replace("&hellip;","&#133;")
    final = final.replace("&eacute;","e")
    final = final.replace("&nbsp;", " ")
    final = final.replace("&#8220;",'&quot;')
    final = final.replace("&#8221;",'&quot;')
    final = final.replace("&#8216;","'")
    final = final.replace("&#8217;","'")

    #Is this the smartest thing to do? No
    #Am I scared of breaking some weird encoding that might be making use of &?
    #...yes
    final = final.replace("& ","&amp; ")
    final = final.replace("A&M","A&amp;M")
    final = final.replace("A&T","A&amp;T")
    final = final.replace("T&T","T&amp;T")

    final = final.replace("&oacute;","o")
    final = final.replace("&uacute;","u")
    final = final.replace("&ntilde;","n")
    final = final.replace("&aacute;","a")
    final = final.replace("&egrave;","e")
    final = final.replace("&uuml;","u")
    final = final.replace("&iacute;","ia")
    final = final.replace("&ccedil;","c")
    final = final.replace("&agrave;","a")

    final = final.encode("utf-8", "ignore")
    f = open(filepath, "w")
    f.write(final)

    return final

#State Offices is in the new data, but not in the old one. I should look into that

def tag_check(tag, text):
    if text and len(text) > 5:
        return "<"+tag+">"+escape_tags(text)+"</"+tag+">"
    else:
        return "<"+tag+">"+"</"+tag+">"

def ordinal(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def ordinal_string(num):
    num = int(num)
    nth = {
        0: "Zeroth",
        1: "First",
        2: "Second",
        3: "Third",
        4: "Fourth",
        5: "Fifth",
        6: "Sixth",
        7: "Seventh",
        8: "Eighth",
        9: "Ninth",
        10: "Tenth",
        11: "Eleventh",
        12: "Twelfth",
        13: "Thirteenth",
        14: "Fourteenth",
        15: "Fifteenth",
        16: "Sixteenth",
        17: "Seventeenth",
        18: "Eighteenth",
        19: "Nineteenth",
        20: "Twentieth",
        21: "Twenty first",
        22: "Twenty second",
        23: "Twenty third",
        24: "Twenty fourth",
        25: "Twenty fifth",
        26: "Twenty sixth",
        27: "Twenty seventh",
        28: "Twenty eighth",
        29: "Twenty ninth",
        30: "Thirtieth",
        31: "Thirty first",
        32: "Thirty second",
        33: "Thirty third",
        34: "Thirty fourth",
        35: "Thirty fifth",
        36: "Thirty sixth",
        37: "Thirty seventh",
        38: "Thirty eighth",
        39: "Thirty ninth",
        40: "Fortieth",
    }
    if num <= 40:
        return nth[num]
    else:
        return int(num)

def tag_set(attr, value):
    value = unicode(value)
    value = value.replace("<","&lt;")
    value = value.replace(">", "&gt;")
    value = value.replace('"', "&quot;")
    value = value.replace("&", "&amp;")
    value = value.replace("'", "&apos;")
    
    if not value:
        value = ""
    return str(attr)+'="'+str(value)+'" '

def get_presidential_politics(state):
    return tag_check("presidential-politics", AapState.objects.get(postal=state).pres_politics)

def get_congressional_districting(state):
    return tag_check("congressional-districting", AapState.objects.get(postal=state).cong_districting)

def get_congressional_lineup(state):
    state_id = AapState.objects.get(postal=state).area_id
    lineups = AapCongressionallineup.objects.filter(state_id=state_id)
    final = "<congressional-lineup>"
    for lineup in lineups:
        congress = AapCongress.objects.get(id=lineup.congress_id)
        n = congress.number
        ordinal_congress = ordinal(n)
        dems = lineup.democrats
        reps = lineup.republicans
        vacancies = str(lineup.vacancies)
        independents = str(lineup.independents)
        if dems > reps:
            majority = str(dems)+" D"
            minority = str(reps)+"  R"
        else:
            majority = str(reps)+" R"
            minority = str(dems)+" D"
        
        temp = '<lineup '+tag_set("id", n)
        temp += tag_set("congress", ordinal_congress+" Congress Lineup")
        temp += tag_set("majority", majority)
        temp += tag_set("vacants", vacancies)
        temp += tag_set("minority", minority)
        temp += tag_set("independent", independents)
        temp += "/>"
        final += temp
    final += "</congressional-lineup>"
    return final

def get_census(state):
    area_id = AapState.objects.get(postal=state).area_id
    census_fields = AapDemoitem.objects.filter(area_id=area_id)
    final = "<census>"
    for data in census_fields:
        field = AapDemofield.objects.get(id=data.field_id)
        xml_id = field.name
        xml_label = field.label
        xml_description = field.description
        xml_value = data.value
        
        temp = '<field '
        temp += tag_set("id", xml_id)
        temp += tag_set("label", xml_label)
        temp += tag_set("description", xml_description)
        temp += tag_set("value", xml_value)
        temp += " />"
        final += temp
    final += "</census>"
    return final

def get_legislature(state):
    state = AapState.objects.get(postal=state)
    term_limits = "Yes" if state.termlimits else "No"
    legislature = state.legistype
    upper_name = state.upper_chamber_name
    lower_name = state.lower_chamber_name

    upper_d = str(state.house_dems)+" D "
    upper_r = str(state.house_reps)+" R "
    upper_i = str(state.house_indeps)+" I "
    upper_v = str(state.house_vacants)+" V "
    
    lower_d = str(state.house_dems)+" D "
    lower_r = str(state.house_reps)+" R "
    lower_i = str(state.house_indeps)+" I "
    lower_v = str(state.house_vacants)+" V "

    final = "<legislature "
    final += tag_set("term-limits", term_limits)
    final += tag_set("name", legislature)
    final += ">"
    
    final += '<chamber id="upper" type="upper" '
    final += tag_set("name", upper_name)
    final += tag_set("seats", upper_d+upper_r+upper_i+upper_v)
    final += "/>"

    final += '<chamber id="lower" type="lower" '
    final += tag_set("name", lower_name)
    final += tag_set("seats", lower_d+lower_r+lower_i+lower_v)
    final += "/>"

    final += "</legislature>"
    return final

def get_election_results(state):
    area_id = AapState.objects.get(postal=state).area_id
    elections = AapElection.objects.filter(elecarea_id=area_id)
    final = "\n<election-results>"
    for election in elections:
        year = election.elecdate.year
        xml_id = str(year)+"-"
        
        if election.electype == "primary":
            #I need to be janky here because some primaries don't have an associated party (which doesn't make sense)
            try:
                party = AapParty.objects.get(id=election.party_id)     
                xml_id += party.label.lower()+"-primary"
                xml_party_code = party.code
            except:
                xml_id = "Primary"
                xml_party_code = "Primary"
        else:
            xml_id += "general"
            xml_party_code = False
        xml_year = year
        xml_heading = election.electype
        seat = AapSeat.objects.get(id=election.seat_id)
        seat_type = seat.seattype
        

        temp = "\n\t<election "
        temp += tag_set("id", xml_id)
        temp += tag_set("year", year)
        temp += tag_set("heading", xml_heading)
        if xml_party_code:
            temp += tag_set("party", xml_party_code)
        temp += tag_set("seat", seat_type)
        #Sort key? The original data dump finished the election tag with a single digit number called "sort-key" but I can't find this anywhere"
        temp += ">"
        final += temp
        
        results = AapElectionresult.objects.filter(election_id=election.id)
        for result in results:
            temp = "\n\t\t<result "
            try:
                person = AapPerson.objects.get(id=result.person_id)
                xml_id = person.first_name.lower()+"-"+person.last_name.lower()
                xml_person = person.first_name+" "+person.last_name
                xml_last_name = person.last_name
            except:
                #I need to do this hack-y nonsense because the person_id attribute of an election result isn't filled in for sevearl users.
                #I could go through the database and sync the person_id to likely matches (two people with the same name would cause problems
                #...as they do here, but I'd like permission before screwing around with the data
                split = result.label.split()
                if len(split) > 1:
                    xml_person = split[0]+" "+split[1]
                    xml_id = split[0].lower()
                    xml_last_name = split[1]
                else:
                    xml_person = xml_id = xml_last_name = ""
            if result.unopposed:
                xml_unopposed = "Yes"
            else:
                xml_unopposed = "No"
            xml_votes = result.num_votes
            xml_percentage = result.perc_vote
            try:
                party = AapParty.objects.get(id=result.party_id)
                xml_party = party.label
            except:
                party = ""
                xml_party = party
            temp += tag_set("id", xml_id)
            temp += tag_set("person", xml_person)
            temp += tag_set("last-name", xml_last_name)
            temp += tag_set("unopposed", xml_unopposed)
            temp += tag_set("votes", xml_votes)
            temp += tag_set("percentage", xml_percentage)
            temp += tag_set("party", xml_party)
            temp += "/>"
            final += temp
        final += "\n\t</election>"
    final += "\n</election-results>"
    return final

def get_governor(state):
    area_id = AapState.objects.get(postal=state).area_id
    seat = AapSeat.objects.filter(area_id=area_id).filter(seattype="gov")[0]
    tenure = AapTenure.objects.filter(seat_id=seat.id).order_by("-start_date")[0]
    person = AapPerson.objects.get(id=tenure.person_id)
    
    first_name = person.first_name
    last_name = person.last_name
    party = AapParty.objects.get(id=person.party_id).code
    photo_url = person.photo_filename

    final = '\n<governor '+tag_set("first-name", first_name)+tag_set("last-name", last_name)+tag_set("party",party)+tag_set("photo-filename", photo_url)+">"
    final += get_elected_tag(tenure)
    final += get_background_tag(person)
    final += get_career_tag(person)
    final += get_main_office_tag(person)
    final += get_election_results_tag(person)
    final += get_prior_wins_tag(person)
    final += get_narrative_tag(person)
    final += "\n</governor>"
    return final

def get_senators(state):
    area_id = AapState.objects.get(postal=state).area_id
    senate_seats = AapSeat.objects.filter(area_id=area_id).filter(seattype="sen").order_by("-seatrank")
    final = "\n<senators>"
    for seat in senate_seats:
        tenure = AapTenure.objects.filter(seat_id=seat.id).order_by("-start_date")[0]
        person = AapPerson.objects.get(id=tenure.person_id)

        first_name = person.first_name
        last_name = person.last_name
        party = AapParty.objects.get(id=person.party_id).code
        xml_seat_name = "Junior"
        if seat.seatrank:
            xml_seat_name = "Senior"
        xml_id = xml_seat_name.lower()
        xml_seat = xml_id
        xml_first_name = first_name
        xml_last_name = last_name
        xml_party = party
        #Still no photo URL    
    
        temp = "\n\t<senator "+tag_set("id", xml_id)+tag_set("seat", xml_seat)+tag_set("seat-name", xml_seat_name)+tag_set("first-name",first_name)
        temp += tag_set("last-name",last_name)+tag_set("party", xml_party)+tag_set("photo-filename", person.photo_filename)+">"
        temp += get_elected_tag(tenure)
        temp += get_background_tag(person)
        temp += get_career_tag(person)
        temp += get_main_office_tag(person)
        temp += get_election_results_tag(person)
        temp += get_prior_wins_tag(person)
        temp += get_narrative_tag(person)
        temp += "\n\t</senator>"
        final += temp
    final += "\n</senators>"
    return final

def get_representatives(state):
    state_object = AapState.objects.get(postal=state)
    districts = AapDistrict.objects.filter(state_id=state_object.area_id)
    final = "\n<representatives>"
    for district in districts:
        print district.area_id
        seat = AapSeat.objects.filter(seattype='rep').get(area_id=district.area_id)
        tenure = AapTenure.objects.filter(seat_id=seat.id).order_by("-start_date")
        if tenure:
            tenure = tenure[0]
            person = AapPerson.objects.get(id=tenure.person_id)
            area = AapArea.objects.get(id=district.area_id)    
    
            first_name = person.first_name
            last_name = person.last_name
            party = AapParty.objects.get(id=person.party_id)
            district_number = re.sub("[^0-9]", "", area.name)
            if district_number < 10:
                xml_id = "dist-0"+str(district_number)
            else:
                xml_id = "dist-"+str(district_number)
            xml_seat = district_number
            if district_number:
                xml_seat_name = ordinal_string(district_number)
            else:
                xml_seat_name = ""
            xml_page_heading = str(xml_seat_name)+" District"

            temp = "\n\t<representative "+tag_set("id", xml_id)+tag_set("seat", xml_seat)+tag_set("seat-name", xml_seat_name)
            temp += tag_set("page-heading", xml_page_heading)+tag_set("first-name", first_name)+tag_set("last_name",last_name)+tag_set("party", party.code)
            temp += tag_set("photo-filename", person.photo_filename)
            temp += ">"
            temp += get_elected_tag(tenure)
            temp += get_background_tag(person)
            temp += get_career_tag(person)
            temp += get_main_office_tag(person)
            temp += get_election_results_tag(person)
            temp += get_prior_wins_tag(person)
            temp += get_narrative_tag(person)
            temp += get_state_offices_tag(person)
            temp += get_committees_tag(person)
            temp += get_group_ratings_tag(person)
            temp += get_nj_ratings_tag(person)
            temp += get_key_votes_tag(person)
            temp += get_district_tag(person, tenure)
            temp += "\n\t</representative>"
            final += temp
    final += "\n</representatives>"
    return final       
 
def get_elected_tag(tenure):
    final = "\n\t<elected "
    xml_year_elected = "Elected "+str(tenure.yearelected)
    xml_expires = tenure.termexpires
    xml_term_number = ordinal(tenure.termnumber)
    xml_full_term = "Yes" if tenure.fullterm_label else "No"
    final += tag_set("year", xml_year_elected)+tag_set("expires",xml_expires)+tag_set("term-number", xml_term_number)+tag_set("full-term",xml_full_term)+"/>"
    return final

def get_background_tag(person):
    final = "\n\t<background "
    xml_children_label = str(person.children)+" children"
    xml_num_children = person.children
    if xml_num_children == "1":
        xml_children_label = "1 child"
    
    final += tag_set("dob", person.birthdate)
    final += tag_set("birthplace", person.birthplace)
    final += tag_set("hometown", person.hometown)
    final += tag_set("education", person.education)
    final += tag_set("religion", person.religion)
    final += tag_set("marital-status", person.marital_status)
    final += tag_set("spouse", person.spouse)
    final += tag_set("children", person.children)
    final += tag_set("children-label", xml_children_label)
    final += "/>"
    return final 
 
def get_career_tag(person):
    final = "<career>"
    #Political
    final += "<political>"+escape_tags(person.political_career)+"</political>"
    final += "<professional>"+escape_tags(person.professional_career)+"</professional>"
    final += "<military>"+escape_tags(person.military_career)+"</military>"
    final += "</career>"    
    return final    

def get_main_office_tag(person):
    final = "<main-office "
    office = AapPersonoffice.objects.filter(person_id=person.id).filter(type="main").order_by("-modified")
    if office:
        office = office[0]
        final += tag_set("address", office.address)
        final += tag_set("zip", office.zip)
        final += tag_set("phone", office.phone)
        final += tag_set("fax", office.fax)
        final += tag_set("website", person.website)
    final += "/>"
    return final

def get_election_results_tag(person):
    final = "<election-results>"
    election_results = AapElectionresult.objects.filter(person_id=person.id)
    for election_result in election_results:
        election = AapElection.objects.get(id=election_result.election_id)
        temp = "<election "
        election_year = election.elecdate.year
        election_type = election.electype
        if election.party_id:
            party_name = AapParty.objects.get(id=election.party_id).label.lower()
            if party_name:
                election_type=party_name+"-"+election_type
        temp += tag_set("id",str(election_year)+"-"+election_type)
        temp += tag_set("year", str(election_year))
        temp += tag_set("heading", election.electype) #At this point, I've set the election_type to potentially include primary party info
        
        seat = AapSeat.objects.get(id=election.seat_id)
        if seat.seattype == "sen":
            tag_set("seat", "Senate")
        else:
            tag_set("seat","House")
        temp += '>'
        final += temp

        for all_result in AapElectionresult.objects.filter(election_id=election.id):
            #Retrieving ALL election results from elections in which the candidate in question participatedin  
            #Not just the ones that match our candidate
            try:
                candidate = AapPerson.objects.get(id=all_result.person_id)
                first_name = candidate.first_name
                last_name = candidate.last_name
            except:
                label_name = all_result.label.split()
                if len(label_name) > 2:
                    first_name = label_name[0]
                    last_name = label_name[1]
                else:
                    first_name = ""
                    last_name = ""
            temp = "<result "
            temp += tag_set("receipts", str(all_result.totrecs))
            temp += tag_set("id", first_name.lower()+"-"+last_name.lower())
            temp += tag_set("person", first_name+" "+last_name)
            temp += tag_set("last-name", last_name)
            if all_result.unopposed:
                temp += tag_set("unopposed", "True")
            else:
                temp += tag_set("unopposed", "False")
            try:
                party = AapParty.objects.get(id=candidate.party_id).code
            except:
                party = ""
            temp += tag_set("party", party)
            temp += "/>"
            final += temp
        final += "</election>"
    final += "</election-results>"
    return final
 
def get_prior_wins_tag(person):
    return "<prior-wins "+tag_set("value", person.prior_wins)+"/>"

def escape_tags(string):
    string = string.replace("<", "&lt;")
    string = string.replace(">", "&gt;")
    return string

def get_state_narrative_tag(state):
    state = AapState.objects.get(postal=state)
    return "<narrative>"+escape_tags(unicode(state.narrative))+"</narrative>"

def get_narrative_tag(person):
    return "<narrative>"+escape_tags(person.narrative)+"</narrative>"

def get_state_offices_tag(person):
    final = "<state-offices>"
    offices = AapPersonoffice.objects.filter(person_id=person.id).filter(type='district').order_by("-modified")
    for office in offices:
        final += "<office "
        final += tag_set("id", office.place.lower())
        final += tag_set("location", office.place)
        final += tag_set("phone", office.phone)
        final += "/>"
    final += "</state-offices>"
    return final

def get_committees_tag(person):
    final = "<committees>"
    committee_assignments = AapCommitteeassignment.objects.filter(person_id=person.id)
    if committee_assignments:
        for assignment in committee_assignments:
            #Checking if this is a sub committee or not
            committee = AapCommittee.objects.get(id=assignment.committee_id)
            if not committee.parent_id:
                temp = "\n<committee "
                temp += tag_set("id", committee.short_name.lower())
                temp += tag_set("name", committee.name)
                temp += ">"
                final += temp
                sub_committees = AapCommittee.objects.filter(parent_id=committee.id)
                for sub_committee in sub_committees:
                    is_member = committee_assignments.filter(id=sub_committee.id)
                    if is_member:
                        temp = "<sub-committee "
                        temp += tag_set("id", sub_committee.short_name.lower())
                        temp += tag_set("name", sub_committee.name)
                        if assignment.is_chair:
                            temp += tag_set("office", "Chair")
                        if assignment.is_rmm:
                            temp += tag_set("office", "rmm")
                        if assignment.is_vicechmn:
                            temp += tag_set("office", "VChmn")
                        temp += "/>"
                        final += temp
                final += "</committee>"
    final += "</committees>"
    return final

def get_group_ratings_tag(person):
    final = "<group-ratings>"
    group_ids = AapPersongrouprating.objects.filter(id=person.id).values("group_id").distinct()
    for group_id in group_ids:
        group = AapInterestgroup.objects.get(id=group_id['group_id'])
        temp = "<group "
        temp += tag_set("id", group.label.lower())
        temp += tag_set("name", group.label)
        temp += tag_set('sort-key', group.sort_key)
        temp += ">"
        final += temp

        ratings = AapPersongrouprating.objects.filter(person_id=person.id).filter(group_id=group.id)
        for rating in ratings:
            temp = "<rating "
            temp += tag_set("id", rating.year)
            temp += tag_set("year", rating.year)
            temp += tag_set("rating", rating.rating)
            temp += "/>"
            final += temp
        final += "</group>"
    final += "</group-ratings>"
    return final

def get_nj_ratings_tag(person):
    final = "<nj-ratings>"
    ratings = AapPersonvoteratingCopy.objects.filter(person_id=person.id)
    for rating in ratings:
        temp = "<rating-year "
        temp += tag_set("id", rating.year)
        temp += tag_set("year", rating.year)
        temp += tag_set("for-lib", rating.lib_for)
        temp += tag_set("com-lib", rating.lib_comp)
        temp += tag_set("soc-lib", rating.lib_soc)
        temp += tag_set("eco-lib", rating.lib_eco)
        temp += tag_set("for-con", rating.con_for)
        temp += tag_set("com-con", rating.con_comp)
        temp += tag_set("soc-con", rating.con_soc)
        temp += tag_set("eco-con", rating.con_eco)
        temp += "/>"
        final += temp
    final += "</nj-ratings>"
    return final

def get_key_votes_tag(person):
    final = "<key-votes>"
    votes = AapPersonvote.objects.filter(person_id=person.id)
    for vote in votes:
        temp = "<vote "
        issue = AapKeyvote.objects.get(id=vote.vote_id)
        temp += tag_set("id", issue.short_name.lower().replace(" ","-"))
        temp += tag_set("title", issue.short_name)
        temp += tag_set("position", vote.position)
        temp += tag_set("year", issue.year)
        temp += tag_set("sort-key", issue.sort_key)
        temp += "/>"
        final += temp
    final += "</key-votes>"
    return final

def get_district_tag(person, tenure):
    seat = AapSeat.objects.get(id=tenure.seat_id)
    area = AapArea.objects.get(id=seat.area_id)
    district = AapDistrict.objects.get(area_id=area.id)

    final = "<district>" 
    #This originally had an id tag for "cookpvi" but I can't find that anywhere in the database. 
    #My inability to do so coincides with a random break in the code that involved a cookpvi variable.
    #Perhaps this was sloppily removed from the database at some time in the past, and is the reason behind several of the broken NStein functions?

    final += "<narrative>"+escape_tags(unicode(district.narrative))+"</narrative>"
   
    final += "<census>"
    census_items = AapDemoitem.objects.filter(area=area)
    for item in census_items:
        field = AapDemofield.objects.get(id=item.field_id)
        temp = "<field "
        temp += tag_set("id", field.name)
        temp += tag_set("label", field.label)
        temp += tag_set("description", field.description)
        temp += tag_set("value", item.value)
        temp += "/>"
        final += temp
    final += "</census>"

    final += "<election-results>"
    elections = AapElection.objects.filter(elecarea_id=district.area_id)
    for election in elections:
        temp = "<election "
        election_year = election.elecdate.year
        election_type = election.electype
        if election.party_id:
            party_name = AapParty.objects.get(id=election.party_id).label.lower()
            if party_name:
                election_type=party_name+"-"+election_type 
        temp += tag_set("id",str(election_year)+"-"+election_type)
        temp += tag_set("year", str(election_year))
        temp += tag_set("heading", election.electype) #At this point, I've set the election_type to potentially include primary party info

        seat = AapSeat.objects.get(id=election.seat_id)
        if seat.seattype == "sen":
            tag_set("seat","Senate")
        else:
            tag_set("seat","House")
        temp += '>'
        final += temp

        for all_result in AapElectionresult.objects.filter(election_id=election.id):
            #Retrieving ALL election results from elections in which the candidate in question participatedin  
            #Not just the ones that match our candidate
            temp = "<result "
            temp += tag_set("receipts", "$"+str(all_result.totrecs))
            try:
                candidate = AapPerson.objects.get(id=all_result.person_id)
                temp += tag_set("id", candidate.first_name.lower()+"-"+candidate.last_name.lower())
                temp += tag_set("person", candidate.first_name+" "+candidate.last_name)
                temp += tag_set("last-name", candidate.last_name)
                try:
                    party = AapParty.objects.get(id=all_result.party_id)
                    temp += tag_set("party", party.code)
                except:
                    temp += tag_set("party", "")
            except:
                label = all_result.label
                if label:
                    label = label.lower().replace(" ","-")
                temp += tag_set("id", str(label))
                temp += tag_set("person",all_result.label)
                try:
                    temp += tag_set("last-name", all_result.label.split(" ")[1])
                except: 
                    temp += tag_set("last-name", all_result.label)
                try:
                    temp += tag_set("party", AapParty.objects.get(id=all_result.party_id).code)
                except:
                    temp += tag_set("party", "")
            if all_result.unopposed:
                temp += tag_set("unopposed","True")
            else:
                temp += tag_set("unopposed", "False")
            
            temp += " />"    
            final += temp    
        final += "</election>"
    final += "</election-results>"
    final += "</district>"
    return final
