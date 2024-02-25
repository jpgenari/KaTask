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
            ]
        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'featured_image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def clean_featured_image(self):
        featured_image = self.cleaned_data.get('featured_image')

        if featured_image:
            # Check if the uploaded file is an image
            content_type = featured_image.content_type.split('/')[0]
            if content_type not in ['image']:
                raise forms.ValidationError('File type is not supported. Please upload an image.')

        return featured_image
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name'
            ]
        