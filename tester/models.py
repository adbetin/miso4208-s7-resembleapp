from django.db import models


# Create your models here.
class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    report_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.created_at)
