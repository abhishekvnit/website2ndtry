from django.db import models

# Create your models here.


class Talcherdb(models.Model):
    sn = models.IntegerField(db_column='Sn', primary_key=True)  # Field name made lowercase.
    task_name = models.TextField(db_column='Task Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_type = models.TextField(db_column='Activity Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planned_start = models.DateField(db_column='Planned Start', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planned_finish = models.DateField(db_column='Planned Finish', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_start = models.DateField(db_column='Actual Start', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_finish = models.DateField(db_column='Actual Finish', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pgma = models.TextField(db_column='PGMA', blank=True, null=True)  # Field name made lowercase.
    parent_wbs_level = models.TextField(db_column='Parent WBS Level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'talcherdb'