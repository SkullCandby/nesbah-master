from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class bank_portal_new(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="bank_portal_new"
    )
    count = models.IntegerField(max_length=200, null=True)
    unlocked_applications = models.CharField(max_length=999, null=False)
    def __dir__(self):
        return self.unlocked_applications
