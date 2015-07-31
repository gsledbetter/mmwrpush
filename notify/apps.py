from django.apps import AppConfig
 
 
class NotifyConfig(AppConfig):
    name = 'notify'
    verbose_name = 'Notify Application'
 
    def ready(self):
        import notify.signals
