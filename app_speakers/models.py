from django.db import models


class Organizations(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'organizations'
        verbose_name = 'Organizations'
        verbose_name_plural = 'Organizations'
        

class SpeakerType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table ='speaker_type'
        verbose_name = 'SpeakerType'
        verbose_name_plural = 'SpeakerType'
        

class Speakers(models.Model):
    conferency = models.ForeignKey('app_conferency.Conferency', on_delete=models.DO_NOTHING, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    speaker_type = models.ForeignKey(SpeakerType,on_delete=models.CASCADE, null=True, blank=True)
    organizations = models.ForeignKey(Organizations,on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    speaker_image = models.ImageField(upload_to='speakers/', blank=True,null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        db_table ='speakers'
        verbose_name = 'Speakers'
        verbose_name_plural = 'Speakers'