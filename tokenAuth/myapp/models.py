from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    token_field = models.CharField(max_length=200, blank=True)
    # created = models.DateTimeField(auto_now_add=True)

# curl -X POST http://localhost:8000/api/tasks/ -d "username=ratul&password=jain"
