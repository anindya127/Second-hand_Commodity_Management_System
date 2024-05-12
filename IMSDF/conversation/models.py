from django.db import models
from django.contrib.auth.models import User

from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="conversation")
    member = models.ManyToManyField(User, related_name="conversation")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_at",]

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="message")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at",]
