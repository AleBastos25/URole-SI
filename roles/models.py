from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
import uuid

class BaseTrackingModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    
    class Meta:
        abstract = True 

class Category(BaseTrackingModel):

    CATEGORIAS = (
        (0, "Festa"),
    )

    name = models.IntegerField(choices=CATEGORIAS,null=True, unique=True)
    slug = models.SlugField(db_index=True, editable=False)
    
    class Meta:
        verbose_name_plural = "Categorias"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.name)


class Role(BaseTrackingModel):
    name = models.CharField(max_length=250, unique=True)
    role_date = models.DateField(null=True)
    role_start_time = models.TimeField(null=True)
    role_end_time = models.TimeField(null=True)
    location = models.CharField(max_length=300)
    address = models.CharField(max_length=100, null=True)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    banner_url = models.TextField(verbose_name="Banner Image URL",blank=True, null=True)
#    category = models.ManyToManyField(Category)
    about = models.TextField(null=True) 
    expired = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Rolês"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Ticket(BaseTrackingModel):
    type = models.CharField(max_length=25)
    price = models.FloatField()
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.role.name+" - "+self.type
    