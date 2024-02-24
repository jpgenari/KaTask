from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'featured_image',
            'category',
            'due_date',
            'priority',
            'completed'
            ]
        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            )
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name'
            ]