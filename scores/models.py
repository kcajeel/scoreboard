from django.db import models

# Create your models here.
class teams(models.Model):
    team_id = models.BigIntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Teams'
        db_table = 'teams'

class targets(models.Model):
    target_id = models.BigIntegerField(primary_key=True, default=0)
    target_host = models.CharField(max_length=255)
    team_id = models.ForeignKey(teams, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'Targets'
        db_table = 'targets'

class ports(models.Model):

    class RESULT_CODES(models.TextChoices):
        S = "SUC", "success"
        F = "FAL", "failure"
        P = "PAR", "partial"
        U = "UNK", "unknown"
        E = "ERR", "error"

    port_id = models.BigIntegerField(primary_key=True, default=0)
    port_number = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    result_code = models.CharField(choices=RESULT_CODES.choices, max_length=3, default=RESULT_CODES.U)
    participant_feedback = models.TextField()
    staff_feedback = models.TextField()
    points_obtained = models.IntegerField(default=0)
    target_id = models.ForeignKey(targets, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = "Ports"
        db_table = 'ports'
