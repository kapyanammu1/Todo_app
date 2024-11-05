from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    llm_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
