from django.db import models

# Create your models here.
class teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    points = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Teams'
        db_table = 'teams'

class targets(models.Model):
    target_id = models.AutoField(primary_key=True)
    target_host = models.CharField(max_length=255)
    team = models.ForeignKey(teams, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'Targets'
        db_table = 'targets'

class ports(models.Model):

    class RESULT_CODES(models.TextChoices):
        PASS = "SUC", "success"
        FAIL = "FAL", "failure"
        WARN = "PAR", "partial"
        UNKNOWN = "UNK", "unknown"
        ERROR = "ERR", "error"

    port_id = models.AutoField(primary_key=True)
    port_number = models.CharField(max_length=255, null=True)
    service_name = models.CharField(max_length=255)
    result_code = models.CharField(choices=RESULT_CODES.choices, max_length=3, default=RESULT_CODES.UNKNOWN)
    participant_feedback = models.TextField()
    staff_feedback = models.TextField()
    points_obtained = models.IntegerField(default=0)
    target = models.ForeignKey(targets, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = "Ports"
        db_table = 'ports'
