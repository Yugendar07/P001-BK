from django.db import models
from django.contrib.auth.models import User

class UserAuthentication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auth_tokens')
    refresh_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - Token"