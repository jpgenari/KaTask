from django import forms
from django.db import models
from .models import Task, Category

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'image',
            'category',
            'due_at',
            'priority',
            ]
        widgets = {
            'due_at': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            # Check if the uploaded file is an image
            if hasattr(image, 'content_type') and image.content_type.split('/')[0] not in ['image']:
                raise forms.ValidationError('File type is not supported. Please upload an image.')
        return image

    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user),  required=False)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name'
            ]
        