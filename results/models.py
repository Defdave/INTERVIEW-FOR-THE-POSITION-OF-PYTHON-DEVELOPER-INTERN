from django.db import models
from django.utils import timezone


class State(models.Model):
    state_id = models.IntegerField(primary_key=True, default=None)
    state_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'state'

class LGA(models.Model):
    lga_id = models.IntegerField(primary_key=True, default=None)
    lga_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'lga'

class Ward(models.Model):
    ward_id = models.IntegerField(primary_key=True, default=None)
    ward_name = models.CharField(max_length=255)
    lga_id = models.IntegerField()

    class Meta:
        db_table = 'ward'

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_name = models.CharField(max_length=255)
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()

    class Meta:
        db_table = 'polling_unit'

class AnnouncedPUResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=255, default=None)
    party_abbreviation = models.CharField(max_length=255)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(default=timezone.now)
    user_ip_address = models.GenericIPAddressField(default='192.168.1.101', blank=True, null=True)

    class Meta:
        db_table = 'announced_pu_results'
