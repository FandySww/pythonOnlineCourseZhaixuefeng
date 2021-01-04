from django.db import models

# Create your models here.
class RunLog(models.Model):
    featureId = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    applicationId = models.CharField(max_length=100)
    createTime = models.CharField(max_length=100)

    def __str__(self):
        return self.featureId+'_'+self.applicationId

class Path(models.Model):
    action = models.CharField(max_length=100)
    shellPath = models.CharField(max_length=100)
    logPath = models.CharField(max_length=100)

    def __str__(self):
        return self.action