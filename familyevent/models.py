from django.db import models
from django.contrib.auth.models import User


class familyevent(models.Model):
  name = models.CharField(max_length = 100, unique=True)
  description = models.CharField(max_length=255)
  location = models.CharField(max_length = 100, unique=True)
  eventdate = models.DateTimeField(null=True)
  created_by = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)

  def __str__(self):
        return self.name

class eventsupply(models.Model):
  name = models.CharField(max_length = 100, unique=True)
  event = models.ForeignKey(familyevent, null=False, related_name='supply',on_delete=models.RESTRICT)
  description = models.CharField(max_length=255,null=True)
  quantity = models.IntegerField(null=True)
  location = models.CharField(max_length = 100,null=True)
  updated_date = models.DateTimeField(null=True)
  prepared = models.ForeignKey(User, null=True, related_name='supply', on_delete=models.RESTRICT)
  created_by = models.ForeignKey(User, null=True,  related_name='+', on_delete=models.RESTRICT)
  status = models.IntegerField(null=False, default=0)

