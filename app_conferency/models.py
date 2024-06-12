from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Conferency(models.Model):
    conf_theme = models.CharField(max_length=255, blank=True, null=True)
    conf_title = models.CharField(max_length=255, blank=True, null=True)
    conf_description = models.TextField(blank=True, null=True)
    conf_date = models.DateField(blank=True, null=True)
    conf_location = models.CharField(max_length=255, blank=True, null=True)
    conf_day = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(31)])
    
    def __str__(self):
        return self.conf_title
    
    
    class Meta:
        db_table = 'conferency'
        verbose_name = 'Conferency'
        verbose_name_plural = 'Conferency'
        

class Sessions(models.Model):
    conferency = models.ForeignKey(Conferency, on_delete=models.CASCADE, blank=True, null=True)
    session_title = models.CharField(max_length=255, blank=True, null=True)
    session_speaker = models.ForeignKey('app_speakers.Speakers', on_delete=models.DO_NOTHING,blank=True, null=True)
    session_timestamp = models.DateTimeField(blank=True, null=True)
    session_description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.session_title
    
    
    class Meta:
        db_table ='sessions'
        verbose_name = 'Sessions'
        verbose_name_plural = 'Sessions'
        
class ConferencyAgenda(models.Model):
    conferency = models.ForeignKey(Conferency, on_delete=models.CASCADE, blank=True, null=True)
    agenda_day = models.DateTimeField(blank=True, null=True)
    agenda_time = models.DateTimeField(blank=True, null=True)
    agenda_title = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.agenda_title
    
    
    class Meta:
        db_table = 'conferency_agenda'
        verbose_name = 'Conferency Agenda'
        verbose_name_plural = 'Conferency Agenda'


class ConferencySections(models.Model):
    conferency = models.ForeignKey(Conferency, on_delete=models.CASCADE, blank=True, null=True)
    section_title = models.CharField(max_length=255, blank=True, null=True)
    section_description = models.TextField(blank=True, null=True)
    section_logo = models.ImageField(upload_to='sections/',blank=True, null=True)
    
    def __str__(self) -> str:
        return self.section_title
    
    
    class Meta:
        db_table = 'conferency_sections'
        verbose_name = 'Conferency Sections'
        verbose_name_plural = 'Conferency Sections'
        

class Partners(models.Model):
    conferency = models.ForeignKey(Conferency, on_delete=models.CASCADE, blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    partner_logo = models.ImageField(upload_to='partners/',blank=True, null=True)
    
    def __str__(self) -> str:
        return self.partner_name
    
    
    class Meta:
        db_table = 'partners'
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'
        
class SubmissionFee(models.Model):
    conferency = models.ForeignKey(Conferency, on_delete=models.CASCADE, blank=True, null=True)
    sub_for = models.CharField(max_length=255, blank=True, null=True)
    sub_price = models.FloatField(null=True, blank=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    sub_description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.sub_title
    
    class Meta:
        db_table = 'submission_fee'
        verbose_name = 'Submission Fee'
        verbose_name_plural = 'Submission Fee'