import uuid

from django.db import models
from django.contrib.auth.models import User


class Interaction(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="interactions")
    question = models.TextField()
    llm_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"Interaction - {self.id}"

class Audit(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PROCESSING = "PROCESSING", "Processing"
        COMPLETED = "COMPLETED", "Completed"
        FAILED = "FAILED", "Failed"

    class TemporalType(models.TextChoices):
        STABLE = "STABLE", "Stable"
        TIME_SENSITIVE = "TIME_SENSITIVE", "Time Sensitive"

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    interaction = models.ForeignKey(Interaction,on_delete=models.CASCADE,related_name="audits")
    topic = models.CharField(max_length=255,blank=True)
    subject_area = models.CharField(max_length=100,blank=True)
    temporal_type = models.CharField(max_length=20,choices=TemporalType.choices,blank=True)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    error_message = models.TextField(blank=True)
    started_at = models.DateTimeField(null=True,blank=True)
    completed_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audit - {self.id} ({self.status})"