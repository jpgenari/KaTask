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
        
        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            # Fetch existing categories for the current user
            existing_categories = Category.objects.filter(user=self.instance.user)
            # Create a tuple list for the choices
            category_choices = [(category.id, category.category_name) for category in existing_categories]
            # Add an empty option for "select or add new"
            category_choices.insert(0, ('', 'Select or Add New'))
            # Set the choices for the category field
            self.fields['category'].choices = category_choices
            
        def clean(self):
            cleaned_data = super().clean()
            category = cleaned_data.get('category')
            new_category = cleaned_data.get('new_category')

            if not category and not new_category:
                raise forms.ValidationError('Please select an existing category or enter a new one.')

            return cleaned_data
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name'
            ]