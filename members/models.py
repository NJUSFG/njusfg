from django.db import models
import datetime

# Create your models here.

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    email_addr = model.EmailField()
    identity = model.CharField(max_length=100)
    title = model.CharField(max_length=100)
    protrait = model.ImageField(upload_to='uploads/')
    research_interests = model.TextField()
    cv = model.FileField(upload_to='uploads/')
    join_date = model.DateField()
    leave_date = model.DateField()

    def __str__(self):
        return self.full_name

    def is_active(self):
        today = datetime.date.today()
        return self.leave_date and self.leave_date < today

