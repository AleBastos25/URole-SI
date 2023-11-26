from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid


class Category(models.Model):
    
    ROLE_CATEGORIES = (
        ("Festa", "Festa"),
        ("Funk", "Funk"),
        ("Trap", "Trap") #! Preencher
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, choices=ROLE_CATEGORIES, unique=True)
    
    class Meta:
        verbose_name_plural = "Categorias"
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name 


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True)
    role_date = models.DateField(null=True)
    role_start_time = models.TimeField(null=True)
    role_end_time = models.TimeField(null=True)
    location = models.CharField(max_length=300)
    address = models.CharField(max_length=100, null=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    banner_url = models.TextField(verbose_name="Banner Image URL",blank=True, null=True)
    category = models.ManyToManyField(Category)
    about = models.TextField(null=True)
    expired = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Rolês"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=25)
    price = models.FloatField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.role.name+" - "+self.type
    