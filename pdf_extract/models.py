from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_file_extension

# Create your models here.
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Document(models.Model):
    document = models.FileField(upload_to='documents/%Y/%m/%d/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ExtractedText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extract = models.TextField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
