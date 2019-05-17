from django.db import models
import datetime

# Create your models here.

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    email_addr = models.EmailField()
    identity = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    protrait = models.ImageField(upload_to='uploads/')
    research_interests = models.TextField()
    cv = models.FileField(upload_to='uploads/')
    join_date = models.DateField()
    leave_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.full_name

    #def is_active(self):
    #    today = datetime.date.today()
    #    return self.leave_date and self.leave_date < today

