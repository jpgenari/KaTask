from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'category',
            'due_at',
            'priority',
            ]
        widgets = {
            'due_at': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        }

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
        