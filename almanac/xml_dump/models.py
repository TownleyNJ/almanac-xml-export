# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AapArea(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey('AapDatasource', related_name='datasource_aaparea', blank=True, null=True)
    areatype = models.CharField(max_length=10)
    name = models.CharField(max_length=255, blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_area'


class AapAreamap(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey('AapDatasource', related_name='datasource_aapareamap', blank=True, null=True)
    area = models.ForeignKey(AapArea)
    filename = models.CharField(max_length=255)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_areamap'


class AapCommittee(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey('AapDatasource', related_name='datasource_aapcomittee', blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    short_name = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    website = models.CharField(max_length=255, blank=True)
    room_number = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    chamber = models.CharField(max_length=6)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_committee'


class AapCommitteeassignment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey('AapDatasource', related_name='datasource_aapcommitteeassignment', blank=True, null=True)
    committee = models.ForeignKey(AapCommittee)
    person = models.ForeignKey('AapPerson', related_name='person_aapcommitteeassignment')
    rank = models.IntegerField(blank=True, null=True)
    is_chair = models.NullBooleanField(default=None)
    is_rmm = models.NullBooleanField(default=None)
    is_vicechmn = models.NullBooleanField(default=None)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_committeeassignment'


class AapCongress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey('AapDatasource', related_name='datasource_aapcongress', blank=True, null=True)
    number = models.IntegerField()
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_congress'


class AapCongressionallineup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey('AapDatasource', related_name='datasource_aapcongressionallineup', blank=True, null=True)
    republicans = models.IntegerField()
    democrats = models.IntegerField()
    independents = models.IntegerField()
    vacancies = models.IntegerField()
    state = models.ForeignKey('AapState', related_name='aapstate_aapcongressionallineup')
    congress = models.ForeignKey(AapCongress)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_congressionallineup'


class AapCyclereceipts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    datasource = models.ForeignKey('AapDatasource', related_name='datasource_aapcyclereceipts', blank=True, null=True)
    edit_notes = models.TextField(blank=True)
    last_updated_by = models.CharField(max_length=255)
    modified = models.DateTimeField()
    published = models.BooleanField(default=None)
    cycle_year = models.IntegerField()
    person = models.ForeignKey('AapPerson', related_name='person_aapcyclereceipts')
    receipts = models.FloatField()
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_cyclereceipts'


class AapDatasource(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'aap_datasource'


class AapDemofield(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    name = models.CharField(max_length=40)
    label = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    datatype = models.CharField(max_length=10, blank=True)
    realm = models.CharField(max_length=2, blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_demofield'


class AapDemoitem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    area = models.ForeignKey(AapArea)
    field = models.ForeignKey(AapDemofield)
    value = models.CharField(max_length=255, blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_demoitem'


class AapDistrict(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    area = models.ForeignKey(AapArea, primary_key=True)
    state = models.ForeignKey('AapState', related_name='aapstate_aapdistrict')
    number = models.CharField(max_length=20)
    narrative = models.TextField(blank=True)
    polygon = models.TextField(blank=True)
    encoded_polyline = models.TextField(blank=True)
    distupdate = models.TextField(blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)
    geographic_label = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'aap_district'


class AapElection(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    seat = models.ForeignKey('AapSeat')
    electype = models.CharField(max_length=40)
    elecsubtype = models.CharField(max_length=255, blank=True)
    elecarea = models.ForeignKey(AapArea, blank=True, null=True)
    elecdate = models.DateField(blank=True, null=True)
    total_votes = models.IntegerField(blank=True, null=True)
    party = models.ForeignKey('AapParty', blank=True, null=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_election'


class AapElectionresult(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    election = models.ForeignKey(AapElection)
    person = models.ForeignKey('AapPerson', blank=True, null=True)
    label = models.CharField(max_length=50, blank=True)
    party = models.ForeignKey('AapParty', blank=True, null=True)
    party_label = models.CharField(max_length=255, blank=True)
    num_votes = models.IntegerField(blank=True, null=True)
    perc_vote = models.FloatField(blank=True, null=True)
    expenditures = models.IntegerField(blank=True, null=True)
    totrecs = models.IntegerField(blank=True, null=True)
    paccontrib = models.IntegerField(blank=True, null=True)
    totindcontrib = models.IntegerField(blank=True, null=True)
    cashend = models.IntegerField(blank=True, null=True)
    debtsowed = models.IntegerField(blank=True, null=True)
    nominated = models.NullBooleanField(default=None)
    unopposed = models.NullBooleanField(default=None)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_electionresult'


class AapInterestgroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    label = models.CharField(max_length=10)
    sort_key = models.IntegerField(blank=True, null=True)
    last_edited = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'aap_interestgroup'


class AapKeyvote(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    chamber = models.CharField(max_length=1)
    year = models.CharField(max_length=4)
    rollcall = models.CharField(max_length=5)
    bill_number = models.CharField(max_length=20)
    short_name = models.CharField(max_length=60)
    sort_key = models.IntegerField(blank=True, null=True)
    vote_desc = models.TextField(blank=True)
    in_current_edition = models.BooleanField(default=None)
    last_edited = models.DateTimeField(blank=True, null=True)
    hide_from_website = models.BooleanField(default=None)

    class Meta:
        managed = False
        db_table = 'aap_keyvote'


class AapParty(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    code = models.CharField(max_length=255)
    abbrev = models.CharField(max_length=255, blank=True)
    label = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_party'


class AapPerson(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    prefix = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255, blank=True)
    maiden_name = models.CharField(max_length=255, blank=True)
    suffix = models.CharField(max_length=255, blank=True)
    nj_first_name = models.CharField(max_length=255, blank=True)
    nj_last_name = models.CharField(max_length=255, blank=True)
    fec_id = models.CharField(max_length=9, blank=True)
    legacy_id = models.IntegerField(blank=True, null=True)
    bioguide_id = models.CharField(max_length=10, blank=True)
    govtrack_id = models.CharField(max_length=10, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=255, blank=True)
    hometown = models.CharField(max_length=255, blank=True)
    education = models.TextField(blank=True)
    religion = models.TextField(blank=True)
    marital_status = models.CharField(max_length=255, blank=True)
    spouse = models.CharField(max_length=255, blank=True)
    children = models.CharField(max_length=255, blank=True)
    military_career = models.TextField(blank=True)
    political_career = models.TextField(blank=True)
    professional_career = models.TextField(blank=True)
    website = models.CharField(max_length=255, blank=True)
    narrative = models.TextField(blank=True)
    party = models.ForeignKey(AapParty, blank=True, null=True)
    caucuses_with = models.ForeignKey(AapParty, related_name='caucuses_with_aapperson', blank=True, null=True)
    leadership_post = models.CharField(max_length=255, blank=True)
    photo_filename = models.CharField(max_length=255, blank=True)
    prior_wins = models.TextField(blank=True)
    url_name = models.CharField(max_length=255, blank=True)
    free_access = models.BooleanField(default=None)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_person'


class AapPersongrouprating(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    person = models.ForeignKey(AapPerson)
    group = models.ForeignKey(AapInterestgroup)
    year = models.IntegerField()
    rating = models.IntegerField(blank=True, null=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_persongrouprating'


class AapPersonoffice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    person = models.ForeignKey(AapPerson)
    type = models.CharField(max_length=8)
    place = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    fax = models.CharField(max_length=13, blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_personoffice'


class AapPersonvote(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    person = models.ForeignKey(AapPerson)
    vote = models.ForeignKey(AapKeyvote)
    position = models.CharField(max_length=2)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_personvote'


class AapPersonvoterating(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    person = models.ForeignKey(AapPerson)
    year = models.IntegerField()
    lib_eco = models.IntegerField(blank=True, null=True)
    lib_for = models.IntegerField(blank=True, null=True)
    lib_soc = models.IntegerField(blank=True, null=True)
    lib_comp = models.FloatField(blank=True, null=True)
    lib_rank = models.IntegerField(blank=True, null=True)
    con_eco = models.IntegerField(blank=True, null=True)
    con_for = models.IntegerField(blank=True, null=True)
    con_soc = models.IntegerField(blank=True, null=True)
    con_comp = models.FloatField(blank=True, null=True)
    con_rank = models.IntegerField(blank=True, null=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_personvoterating'


class AapPersonvoteratingCopy(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource_id = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField()
    year = models.IntegerField()
    lib_eco = models.IntegerField(blank=True, null=True)
    lib_for = models.IntegerField(blank=True, null=True)
    lib_soc = models.IntegerField(blank=True, null=True)
    lib_comp = models.FloatField(blank=True, null=True)
    lib_rank = models.IntegerField(blank=True, null=True)
    con_eco = models.IntegerField(blank=True, null=True)
    con_for = models.IntegerField(blank=True, null=True)
    con_soc = models.IntegerField(blank=True, null=True)
    con_comp = models.FloatField(blank=True, null=True)
    con_rank = models.IntegerField(blank=True, null=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_personvoterating_copy'


class AapPhoto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    person = models.ForeignKey(AapPerson)
    collection = models.CharField(max_length=20)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_photo'


class AapPhotoversion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    photo = models.ForeignKey(AapPhoto)
    file = models.CharField(max_length=100)
    scheme = models.CharField(max_length=20)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_photoversion'


class AapSeat(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    area = models.ForeignKey(AapArea, blank=True, null=True)
    seattype = models.CharField(max_length=4)
    seatrank = models.CharField(max_length=2, blank=True)
    sen_class = models.CharField(max_length=3, blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_seat'


class AapState(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    area = models.ForeignKey(AapArea, primary_key=True)
    postal = models.CharField(max_length=2)
    narrative = models.TextField(blank=True)
    pres_politics = models.TextField(blank=True)
    cong_districting = models.TextField(blank=True)
    legistype = models.CharField(max_length=50, blank=True)
    termlimits = models.NullBooleanField(default=None)
    upper_chamber_name = models.CharField(max_length=50, blank=True)
    lower_chamber_name = models.CharField(max_length=50, blank=True)
    senate_seats = models.IntegerField(blank=True, null=True)
    senate_dems = models.IntegerField(blank=True, null=True)
    senate_reps = models.IntegerField(blank=True, null=True)
    senate_indeps = models.IntegerField(blank=True, null=True)
    senate_vacants = models.IntegerField(blank=True, null=True)
    house_seats = models.IntegerField(blank=True, null=True)
    house_dems = models.IntegerField(blank=True, null=True)
    house_reps = models.IntegerField(blank=True, null=True)
    house_indeps = models.IntegerField(blank=True, null=True)
    house_vacants = models.IntegerField(blank=True, null=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_state'


class AapTenure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    person = models.ForeignKey(AapPerson)
    seat = models.ForeignKey(AapSeat)
    start_date = models.DateField()
    effective_start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    effective_end_date = models.DateField(blank=True, null=True)
    termexpires = models.CharField(max_length=15, blank=True)
    electedlabel = models.CharField(max_length=40, blank=True)
    monthelected = models.CharField(max_length=20, blank=True)
    yearelected = models.IntegerField(blank=True, null=True)
    termnumber = models.IntegerField(blank=True, null=True)
    fullterm_label = models.NullBooleanField(default=None)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_tenure'


class AapUpdate(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_updated_by = models.CharField(max_length=255)
    published = models.BooleanField(default=None)
    edit_notes = models.TextField(blank=True)
    datasource = models.ForeignKey(AapDatasource, blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    image_url = models.CharField(max_length=2000, blank=True)
    url = models.CharField(max_length=512, blank=True)
    last_edited = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aap_update'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey('AuthUser')
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'auth_message'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=None)
    is_active = models.BooleanField(default=None)
    is_superuser = models.BooleanField(default=None)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Censusdata(models.Model):
    censusdataid = models.IntegerField(primary_key=True)
    censusvalue = models.CharField(max_length=40, blank=True)
    year = models.CharField(max_length=40, blank=True)
    censusdatatypeid = models.ForeignKey('Censusdatatypelut', db_column='censusdatatypeid')
    districtid = models.ForeignKey('Districts', db_column='districtid', blank=True, null=True)
    locationid = models.ForeignKey('Locations', db_column='locationid')

    class Meta:
        managed = False
        db_table = 'censusdata'


class Censusdatatypelut(models.Model):
    censusdatatypeid = models.IntegerField(primary_key=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=40, blank=True)
    itemname = models.CharField(max_length=40, blank=True)
    bottomrange = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    toprange = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    itemtype = models.CharField(max_length=16, blank=True)
    hivalue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    lovalue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'censusdatatypelut'


class Committeemembers(models.Model):
    personid = models.ForeignKey('People', db_column='personid')
    committeeid = models.ForeignKey('Committees', db_column='committeeid')
    office = models.CharField(max_length=40, blank=True)
    rank = models.SmallIntegerField(blank=True, null=True)
    chmnexpires = models.CharField(max_length=16, blank=True)

    class Meta:
        managed = False
        db_table = 'committeemembers'


class Committees(models.Model):
    committeeid = models.IntegerField(primary_key=True)
    parentid = models.IntegerField()
    committeename = models.CharField(max_length=255, blank=True)
    officebuilding = models.CharField(max_length=40, blank=True)
    roomnumber = models.CharField(max_length=16, blank=True)
    website = models.CharField(max_length=127, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    committeetype = models.CharField(max_length=16, blank=True)
    republicanseats = models.SmallIntegerField(blank=True, null=True)
    republicanmembers = models.SmallIntegerField(blank=True, null=True)
    democratseats = models.SmallIntegerField(blank=True, null=True)
    democratmembers = models.SmallIntegerField(blank=True, null=True)
    otherseats = models.SmallIntegerField(blank=True, null=True)
    othermembers = models.SmallIntegerField(blank=True, null=True)
    representativeseats = models.SmallIntegerField(blank=True, null=True)
    representativemembers = models.SmallIntegerField(blank=True, null=True)
    senatorseats = models.SmallIntegerField(blank=True, null=True)
    senatormembers = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'committees'


class Congleaders(models.Model):
    congleaderid = models.IntegerField(primary_key=True)
    body = models.CharField(max_length=16, blank=True)
    title = models.CharField(max_length=127, blank=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    personid = models.ForeignKey('People', db_column='personid')

    class Meta:
        managed = False
        db_table = 'congleaders'


class Districts(models.Model):
    districtid = models.IntegerField(primary_key=True)
    locationid = models.ForeignKey('Locations', db_column='locationid')
    representativeid = models.ForeignKey('People', related_name='representativeid_districts', db_column='representativeid')
    priorrepresentativeid = models.ForeignKey('People', db_column='priorrepresentativeid', blank=True, null=True)
    districtnumber = models.SmallIntegerField(blank=True, null=True)
    priordistnumber = models.SmallIntegerField(blank=True, null=True)
    districtwriteup = models.TextField(blank=True)
    districtupdate = models.TextField(blank=True)
    cookpvi = models.CharField(max_length=16, blank=True)
    created = models.DateField(blank=True, null=True)
    lastchanged = models.DateField(blank=True, null=True)
    factchecked = models.DateField(blank=True, null=True)
    lastsentweb = models.DateField(blank=True, null=True)
    lastpublishedprint = models.DateField(blank=True, null=True)
    locationcode = models.CharField(max_length=16)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'districts'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoFlatpage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField(default=None)
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField(default=None)

    class Meta:
        managed = False
        db_table = 'django_flatpage'


class DjangoFlatpageSites(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    flatpage = models.ForeignKey(DjangoFlatpage)
    site = models.ForeignKey('DjangoSite')

    class Meta:
        managed = False
        db_table = 'django_flatpage_sites'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Edition(models.Model):
    editionid = models.IntegerField(primary_key=True)
    year = models.SmallIntegerField()
    congfirstyear = models.SmallIntegerField(blank=True, null=True)
    congsecondyear = models.SmallIntegerField(blank=True, null=True)
    lastelectionyear = models.SmallIntegerField(blank=True, null=True)
    preselectionyear = models.SmallIntegerField(blank=True, null=True)
    govelectionyear = models.SmallIntegerField(blank=True, null=True)
    senelectionyear = models.SmallIntegerField(blank=True, null=True)
    repelectionyear = models.SmallIntegerField(blank=True, null=True)
    almanacyear = models.SmallIntegerField(blank=True, null=True)
    senmajparty = models.ForeignKey('Parties', db_column='senmajparty', related_name='edition_senmajparty', blank=True, null=True)
    senminparty = models.ForeignKey('Parties', db_column='senminparty', related_name='edition_senminparty', blank=True, null=True)
    housemajpary = models.ForeignKey('Parties', db_column='housemajpary', related_name='edition_housemajparty', blank=True, null=True)
    houseminparty = models.ForeignKey('Parties', db_column='houseminparty', related_name='edition_houseminparty', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edition'


class Electionresults(models.Model):
    electionresultid = models.IntegerField(primary_key=True)
    person = models.CharField(max_length=127, blank=True)
    votes = models.IntegerField(blank=True, null=True)
    percent = models.SmallIntegerField(blank=True, null=True)
    nominated = models.NullBooleanField(default=None)
    unopposed = models.NullBooleanField(default=None)
    electionid = models.ForeignKey('Elections', db_column='electionid')
    party = models.CharField(max_length=40, blank=True)
    position = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electionresults'


class Elections(models.Model):
    electionid = models.IntegerField(primary_key=True)
    districtid = models.ForeignKey(Districts, db_column='districtid', blank=True, null=True)
    locationid = models.ForeignKey('Locations', db_column='locationid')
    sortorder = models.SmallIntegerField(blank=True, null=True)
    seattype = models.CharField(max_length=16)
    electiondistrict = models.SmallIntegerField(blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    excludeinclude = models.SmallIntegerField(blank=True, null=True)
    heading = models.CharField(max_length=127, blank=True)

    class Meta:
        managed = False
        db_table = 'elections'


class Finances(models.Model):
    financesid = models.IntegerField(primary_key=True)
    personid = models.ForeignKey('People', db_column='personid')
    seattype = models.CharField(max_length=16)
    year = models.SmallIntegerField(blank=True, null=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    position = models.SmallIntegerField(blank=True, null=True)
    receipts = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    expended = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    pacs = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    individuals = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    coh = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    debts = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finances'


class Groupratings(models.Model):
    groupratingid = models.IntegerField(primary_key=True)
    personid = models.ForeignKey('People', db_column='personid')
    groupratingheadid = models.ForeignKey('Groupratingslut', db_column='groupratingheadid')
    rating1 = models.CharField(max_length=4, blank=True)
    rating2 = models.CharField(max_length=4, blank=True)
    rating3 = models.CharField(max_length=4, blank=True)
    rating4 = models.CharField(max_length=4, blank=True)
    rating5 = models.CharField(max_length=4, blank=True)
    rating6 = models.CharField(max_length=4, blank=True)
    rating7 = models.CharField(max_length=4, blank=True)
    rating8 = models.CharField(max_length=4, blank=True)
    rating9 = models.CharField(max_length=4, blank=True)
    rating10 = models.CharField(max_length=4, blank=True)
    rating11 = models.CharField(max_length=4, blank=True)
    rating12 = models.CharField(max_length=4, blank=True)
    rating13 = models.CharField(max_length=4, blank=True)
    rating14 = models.CharField(max_length=4, blank=True)
    rating15 = models.CharField(max_length=4, blank=True)
    rating16 = models.CharField(max_length=4, blank=True)
    rating17 = models.CharField(max_length=4, blank=True)
    rating18 = models.CharField(max_length=4, blank=True)
    rating19 = models.CharField(max_length=4, blank=True)
    rating20 = models.CharField(max_length=4, blank=True)
    rating21 = models.CharField(max_length=4, blank=True)
    rating22 = models.CharField(max_length=4, blank=True)
    rating23 = models.CharField(max_length=4, blank=True)
    rating24 = models.CharField(max_length=4, blank=True)
    rating25 = models.CharField(max_length=4, blank=True)
    rating26 = models.CharField(max_length=4, blank=True)
    rating27 = models.CharField(max_length=4, blank=True)
    rating28 = models.CharField(max_length=4, blank=True)
    rating29 = models.CharField(max_length=4, blank=True)
    rating30 = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'groupratings'


class Groupratingslut(models.Model):
    groupratingheadid = models.IntegerField(primary_key=True)
    year = models.SmallIntegerField(blank=True, null=True)
    head1 = models.CharField(max_length=40, blank=True)
    head2 = models.CharField(max_length=40, blank=True)
    head3 = models.CharField(max_length=40, blank=True)
    head4 = models.CharField(max_length=40, blank=True)
    head5 = models.CharField(max_length=40, blank=True)
    head6 = models.CharField(max_length=40, blank=True)
    head7 = models.CharField(max_length=40, blank=True)
    head8 = models.CharField(max_length=40, blank=True)
    head9 = models.CharField(max_length=40, blank=True)
    head10 = models.CharField(max_length=40, blank=True)
    head11 = models.CharField(max_length=40, blank=True)
    head12 = models.CharField(max_length=40, blank=True)
    head13 = models.CharField(max_length=40, blank=True)
    head14 = models.CharField(max_length=40, blank=True)
    head15 = models.CharField(max_length=40, blank=True)
    head16 = models.CharField(max_length=40, blank=True)
    head17 = models.CharField(max_length=40, blank=True)
    head18 = models.CharField(max_length=40, blank=True)
    head19 = models.CharField(max_length=40, blank=True)
    head20 = models.CharField(max_length=40, blank=True)
    head21 = models.CharField(max_length=40, blank=True)
    head22 = models.CharField(max_length=40, blank=True)
    head23 = models.CharField(max_length=40, blank=True)
    head24 = models.CharField(max_length=40, blank=True)
    head25 = models.CharField(max_length=40, blank=True)
    head26 = models.CharField(max_length=40, blank=True)
    head27 = models.CharField(max_length=40, blank=True)
    head28 = models.CharField(max_length=40, blank=True)
    head29 = models.CharField(max_length=40, blank=True)
    head30 = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'groupratingslut'


class Keyvotes(models.Model):
    keyvoteid = models.IntegerField(primary_key=True)
    personid = models.ForeignKey('People', db_column='personid')
    keyvoteheadid = models.ForeignKey('Keyvoteslut', db_column='keyvoteheadid')
    vote1 = models.CharField(max_length=16, blank=True)
    vote2 = models.CharField(max_length=16, blank=True)
    vote3 = models.CharField(max_length=16, blank=True)
    vote4 = models.CharField(max_length=16, blank=True)
    vote5 = models.CharField(max_length=16, blank=True)
    vote6 = models.CharField(max_length=16, blank=True)
    vote7 = models.CharField(max_length=16, blank=True)
    vote8 = models.CharField(max_length=16, blank=True)
    vote9 = models.CharField(max_length=16, blank=True)
    vote10 = models.CharField(max_length=16, blank=True)
    vote11 = models.CharField(max_length=16, blank=True)
    vote12 = models.CharField(max_length=16, blank=True)
    vote13 = models.CharField(max_length=16, blank=True)
    vote14 = models.CharField(max_length=16, blank=True)
    vote15 = models.CharField(max_length=16, blank=True)
    vote16 = models.CharField(max_length=16, blank=True)
    vote17 = models.CharField(max_length=16, blank=True)
    vote18 = models.CharField(max_length=16, blank=True)
    vote19 = models.CharField(max_length=16, blank=True)
    vote20 = models.CharField(max_length=16, blank=True)
    vote21 = models.CharField(max_length=16, blank=True)
    vote22 = models.CharField(max_length=16, blank=True)
    vote23 = models.CharField(max_length=16, blank=True)
    vote24 = models.CharField(max_length=16, blank=True)
    vote25 = models.CharField(max_length=16, blank=True)
    vote26 = models.CharField(max_length=16, blank=True)
    vote27 = models.CharField(max_length=16, blank=True)
    vote28 = models.CharField(max_length=16, blank=True)
    vote29 = models.CharField(max_length=16, blank=True)
    vote30 = models.CharField(max_length=16, blank=True)

    class Meta:
        managed = False
        db_table = 'keyvotes'


class Keyvoteslut(models.Model):
    keyvoteheadid = models.IntegerField(primary_key=True)
    year = models.SmallIntegerField(blank=True, null=True)
    office = models.CharField(max_length=16, blank=True)
    head1 = models.CharField(max_length=40, blank=True)
    head2 = models.CharField(max_length=40, blank=True)
    head3 = models.CharField(max_length=40, blank=True)
    head4 = models.CharField(max_length=40, blank=True)
    head5 = models.CharField(max_length=40, blank=True)
    head6 = models.CharField(max_length=40, blank=True)
    head7 = models.CharField(max_length=40, blank=True)
    head8 = models.CharField(max_length=40, blank=True)
    head9 = models.CharField(max_length=40, blank=True)
    head10 = models.CharField(max_length=40, blank=True)
    head11 = models.CharField(max_length=40, blank=True)
    head12 = models.CharField(max_length=40, blank=True)
    head13 = models.CharField(max_length=40, blank=True)
    head14 = models.CharField(max_length=40, blank=True)
    head15 = models.CharField(max_length=40, blank=True)
    head16 = models.CharField(max_length=40, blank=True)
    head17 = models.CharField(max_length=40, blank=True)
    head18 = models.CharField(max_length=40, blank=True)
    head19 = models.CharField(max_length=40, blank=True)
    head20 = models.CharField(max_length=40, blank=True)
    head21 = models.CharField(max_length=40, blank=True)
    head22 = models.CharField(max_length=40, blank=True)
    head23 = models.CharField(max_length=40, blank=True)
    head24 = models.CharField(max_length=40, blank=True)
    head25 = models.CharField(max_length=40, blank=True)
    head26 = models.CharField(max_length=40, blank=True)
    head27 = models.CharField(max_length=40, blank=True)
    head28 = models.CharField(max_length=40, blank=True)
    head29 = models.CharField(max_length=40, blank=True)
    head30 = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'keyvoteslut'


class Locations(models.Model):
    locationid = models.IntegerField(primary_key=True)
    locationname = models.CharField(max_length=40, blank=True)
    almcode = models.CharField(max_length=8, blank=True)
    postalcode = models.CharField(max_length=2, blank=True)
    apstylecode = models.CharField(max_length=16, blank=True)
    map = models.CharField(max_length=127, blank=True)
    presidentid = models.ForeignKey('People', db_column='presidentid',related_name='presidentid_locations', blank=True, null=True)
    vicepresidentid = models.ForeignKey('People', db_column='vicepresidentid',related_name='vicepresidentid_locations', blank=True, null=True)
    governorid = models.ForeignKey('People', db_column='governorid',related_name='governorid_locations', blank=True, null=True)
    srsenatorid = models.ForeignKey('People', db_column='srsenatorid',related_name='srsenatorid_locations', blank=True, null=True)
    jrsenatorid = models.ForeignKey('People', db_column='jrsenatorid',related_name='jrsenatorid_locations', blank=True, null=True)
    electionsdivisionphone = models.CharField(max_length=40, blank=True)
    congfilingdeadline = models.DateField(blank=True, null=True)
    congfilingtbd = models.NullBooleanField(default=None)
    congprimarydate = models.DateField(blank=True, null=True)
    congrunoffdate = models.DateField(blank=True, null=True)
    specialelectiondesc = models.TextField(blank=True)
    statewriteup = models.TextField(blank=True)
    stateupdate = models.TextField(blank=True)
    prespoliticswriteup = models.TextField(blank=True)
    prespoliticsupdate = models.TextField(blank=True)
    congdistrictingwriteup = models.TextField(blank=True)
    congdistrictingupdate = models.TextField(blank=True)
    curcongmajority = models.CharField(max_length=16, blank=True)
    curcongminority = models.CharField(max_length=16, blank=True)
    curcongindep = models.CharField(max_length=40, blank=True)
    priorcongmajority = models.CharField(max_length=16, blank=True)
    priorcongminority = models.CharField(max_length=16, blank=True)
    priorcongindep = models.CharField(max_length=16, blank=True)
    legistermlimits = models.NullBooleanField(default=None)
    statelegname = models.CharField(max_length=40, blank=True)
    upperlegbodyname = models.CharField(max_length=40, blank=True)
    upperlegbodyseats = models.CharField(max_length=16, blank=True)
    lowerlegbodyname = models.CharField(max_length=40, blank=True)
    lowerlegbodyseats = models.CharField(max_length=16, blank=True)
    created = models.DateField(blank=True, null=True)
    lastchanged = models.DateField(blank=True, null=True)
    factchecked = models.DateField(blank=True, null=True)
    lastsentweb = models.DateField(blank=True, null=True)
    lastpublishedprint = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Natjnlratings(models.Model):
    ratingid = models.IntegerField(primary_key=True)
    personid = models.ForeignKey('People', db_column='personid')
    year = models.SmallIntegerField(blank=True, null=True)
    eclib = models.SmallIntegerField(blank=True, null=True)
    eccon = models.SmallIntegerField(blank=True, null=True)
    soclib = models.SmallIntegerField(blank=True, null=True)
    soccon = models.SmallIntegerField(blank=True, null=True)
    forlib = models.SmallIntegerField(blank=True, null=True)
    forcon = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'natjnlratings'


class Offices(models.Model):
    officeid = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    personid = models.ForeignKey('People', db_column='personid')

    class Meta:
        managed = False
        db_table = 'offices'


class Otherdocuments(models.Model):
    documentid = models.IntegerField(primary_key=True)
    document = models.BinaryField(blank=True, null=True)
    sortorder = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    filename = models.CharField(max_length=255, blank=True)
    pagecount = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otherdocuments'


class Parties(models.Model):
    partyid = models.IntegerField(primary_key=True)
    partyname = models.CharField(max_length=40, blank=True)
    partycode = models.CharField(max_length=16, blank=True)

    class Meta:
        managed = False
        db_table = 'parties'


class People(models.Model):
    personid = models.IntegerField(primary_key=True)
    locationid = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=40, blank=True)
    lastname = models.CharField(max_length=40, blank=True)
    suffix = models.CharField(max_length=16, blank=True)
    partyid = models.ForeignKey(Parties, db_column='partyid', blank=True, null=True)
    seattype = models.CharField(max_length=16, blank=True)
    districtnumber = models.SmallIntegerField(blank=True, null=True)
    newlyelected = models.NullBooleanField(default=None)
    atlarge = models.NullBooleanField(default=None)
    status = models.SmallIntegerField(blank=True, null=True)
    yearelected = models.CharField(max_length=40, blank=True)
    termexpires = models.CharField(max_length=16, blank=True)
    termnumber = models.SmallIntegerField(blank=True, null=True)
    fullterm = models.NullBooleanField(default=None)
    highresimage = models.CharField(max_length=127, blank=True)
    lowresimage = models.CharField(max_length=127, blank=True)
    dob = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=40, blank=True)
    education = models.CharField(max_length=255, blank=True)
    hometown = models.CharField(max_length=40, blank=True)
    religion = models.CharField(max_length=40, blank=True)
    maritalstatus = models.CharField(max_length=40, blank=True)
    spouse = models.CharField(max_length=40, blank=True)
    personwriteup = models.TextField(blank=True)
    personupdate = models.TextField(blank=True)
    militarycareer = models.TextField(blank=True)
    politicalcareer = models.TextField(blank=True)
    professionalcareer = models.TextField(blank=True)
    officebuilding = models.CharField(max_length=127, blank=True)
    roomnumber = models.CharField(max_length=16, blank=True)
    zip = models.CharField(max_length=16, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    fax = models.CharField(max_length=40, blank=True)
    email = models.CharField(max_length=127, blank=True)
    website = models.CharField(max_length=127, blank=True)
    groupratingcommenttype = models.SmallIntegerField(blank=True, null=True)
    groupratingcomment = models.CharField(max_length=127, blank=True)
    natjnlcommenttype = models.SmallIntegerField(blank=True, null=True)
    natjnlcomment = models.CharField(max_length=127, blank=True)
    keyvotecommenttype = models.SmallIntegerField(blank=True, null=True)
    keyvotecomment = models.CharField(max_length=127, blank=True)
    created = models.DateField(blank=True, null=True)
    lastchanged = models.DateField(blank=True, null=True)
    lastsentweb = models.DateField(blank=True, null=True)
    lastpublishedprint = models.DateField(blank=True, null=True)
    factchecked = models.DateField(blank=True, null=True)
    postalcode = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'people'


class Photo(models.Model):
    personid = models.ForeignKey(People, db_column='personid', primary_key=True)
    lowimage = models.BinaryField(blank=True, null=True)
    highimage = models.BinaryField(blank=True, null=True)
    lowimagetype = models.CharField(max_length=16, blank=True)
    highimagetype = models.CharField(max_length=16, blank=True)

    class Meta:
        managed = False
        db_table = 'photo'


class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'


class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    role = models.SmallIntegerField(blank=True, null=True)
    username = models.CharField(max_length=40, blank=True)
    firstname = models.CharField(max_length=40, blank=True)
    lastname = models.CharField(max_length=40, blank=True)
    email = models.CharField(max_length=40, blank=True)
    password = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'users'
