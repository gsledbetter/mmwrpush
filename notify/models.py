from django.db import models
from push_notifications.models import APNSDevice, GCMDevice


# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=2048)
    push_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.message


