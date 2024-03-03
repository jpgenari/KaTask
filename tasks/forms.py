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
        '''
        Checks if file provided is image format, otherwise doesn't allow
        submission.
        '''
        image = self.cleaned_data.get('image')

        if image:
            # Check if the uploaded file is an image
            if hasattr(image, 'content_type') and image.content_type.split('/')[0] not in ['image']:
                raise forms.ValidationError('File type is not supported. Please upload an image.')
        return image

    def __init__(self, user, *args, **kwargs):
        '''
        Ensures that 'Category' field in TaskForm is populated with categories
        belonging to logged-in user and also allows task without category.
        Parameters:
        - user: The user for whom the form is being initialized.
        - *args, **kwargs: Additional arguments and keyword arguments that can
        be passed to the form.
        '''
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user),  required=False)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name'
            ]
        