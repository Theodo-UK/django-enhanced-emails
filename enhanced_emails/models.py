import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class SentEmail(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    to = ArrayField(models.EmailField())
    cc = ArrayField(models.EmailField())
    bcc = ArrayField(models.EmailField())

    class Meta:
        get_latest_by = "sent_at"
        ordering = ("-sent_at",)

    def __str__(self):
        return f"{self.__class__.__name__.lower()}:{str(self.uuid)[:6]}"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("enhanced_emails:email", kwargs={"pk": str(self.uuid)})
