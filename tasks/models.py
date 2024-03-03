from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories_created")
    category_name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.category_name

class Task(models.Model):
    """
    Stores a single task entry related to :model:`auth:User`
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_created")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = CloudinaryField('image', default='placeholder')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    due_at = models.DateField(blank=True, null=True)
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')), default=1)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['completed', 'due_at', '-priority', 'created_at']

    def __str__(self):
        return f"{self.title} | added by {self.user}"
    
    