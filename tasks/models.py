from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Task(models.Model):
    """
    Stores a single task entry related to :model:`auth:User`
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_created")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')), default=1)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['due_date', 'created_at']
    
    def __str__(self):
        return f"{self.title} | added by {self.user}"