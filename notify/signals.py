from django.db.models.signals import post_save
from django.dispatch import receiver
from notify.models import Notification
from push_notifications.models import APNSDevice, GCMDevice


# method for updating
@receiver(post_save, sender=Notification)
def push_notification(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))
    ios_devices = APNSDevice.objects.all()
    for device in ios_devices:
        print("name = {},  registration_id = {}".format(device.name, device.registration_id))
    print("Message = ", kwargs['instance'].message)
    ios_devices.send_message(kwargs['instance'].message)
    android_devices = GCMDevice.objects.all()
    android_devices.send_message(kwargs['instance'].message)


# register the signal
#post_save.connect(push_notification, sender=Notification, dispatch_uid="push_notification_count")
