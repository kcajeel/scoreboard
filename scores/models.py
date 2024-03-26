from django.db import models

# Create your models here.
class teams(models.Model):
    name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Teams'

class service_checks(models.Model):
    RESULT_CODES = {
        "S": "sucess",
        "F": "failure",
        "P": "partial",
        "U": "unknown",
        "E": "error"
    }
    team_id = models.IntegerField(default=0)
    target_host = models.CharField(max_length=255)
    result_code = models.CharField(choices=RESULT_CODES, max_length=7)
    participant_feedback = models.TextField()
    staff_feedback = models.TextField()
    created_at = models.DateTimeField()
    class Meta:
        verbose_name_plural = 'Service Checks'

class check_details(models.Model):
    DETAIL_TYPES = {    
        "P": "participant",
        "S": "staff"
    }
    service_check_id = models.IntegerField(),
    detail_type = models.CharField(choices = DETAIL_TYPES, max_length=11)
    detail = models.TextField()
    class Meta:
        verbose_name_plural = 'Check Details'