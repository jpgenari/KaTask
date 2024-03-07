from django.db import models


# Create your models here.
class Features(models.Model):
    """
    Stores a single features text
    """

    icon = models.TextField(max_length=100)
    title = models.TextField(max_length=200)
    content = models.TextField(max_length=500)
    updated_on = models.DateTimeField(auto_now=True)
    display_order = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 13)],
        unique=True
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class HowToUse(models.Model):
    """
    Stores a single how to use text
    """

    icon = models.TextField(max_length=100)
    title = models.TextField(max_length=200)
    content = models.TextField(max_length=500)
    updated_on = models.DateTimeField(auto_now=True)
    display_order = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 13)],
        unique=True
    )

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class UserFeedback(models.Model):
    """
    Stores a single user feedback text
    """

    content = models.TextField(max_length=500)
    author = models.TextField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_on']

    def __str__(self):
        return self.author
