from django.db import models
import datetime

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=255)
    address = models.TextField()
    description = models.CharField(max_length=255)
    createddate = datetime.datetime.now()
    updatedate = datetime.datetime.now()
    disableddate = models.DateTimeField()
    status = models.CharField(max_length=255)

    def __str_(self):
        return self.title

class Activity(models.Model):
    status_choices = (
        ("Pendiente","P"),
        ("Finalizado","F"),
        ("Atrasado","A"),
    )

    property_id = models.ForeignKey(Property,on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    title_activity = models.CharField(max_length=255)
    createddate_act = datetime.datetime.now()
    updateddate_act = datetime.datetime.now()
    status_activity = models.CharField(max_length=255,choices=status_choices,default=1)

    def __str_(self):
        return self.title_activity

class Survey(models.Model):
    activity_id_survey = models.ForeignKey(Activity,on_delete=models.CASCADE)
    answers = models.JSONField()
    createddate_survey = datetime.datetime.now()

    def __str_(self):
        return self.activity_id_survey