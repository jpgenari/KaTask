from django import forms
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
    
    # def __init__(self, *args, user=None, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)

    #     # Filtering categories based on the signed-in user
    #     if user:
    #         self.fields['category'].queryset = Category.objects.filter(user=user)
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name'
            ]
        