from django.db import models

# Create your models here.
class RunLog(models.Model):
    name = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    createTime = models.CharField(max_length=100)

    def __str__(self):
        return self.name