from email.policy import default
from random import choices
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)
class job(models.Model):
    title=models.CharField(max_length=100)
    #location
    job_time=models.CharField(max_length=15,choices=JOB_TYPE)
    Description=models.TextField(max_length=1000)
    published_at=models.TimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.title