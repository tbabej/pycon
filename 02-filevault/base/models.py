from django.db import models
from django.conf import settings

class Submission(models.Model):

    description = models.CharField(max_length=100)
    secret = models.FileField(upload_to=settings.UPLOAD_DIR)

    def save(self, *args, **kwargs):
        super(Submission, self).save(*args, **kwargs)
