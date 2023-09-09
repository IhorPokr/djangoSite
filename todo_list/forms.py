from django import forms
from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,  # Make this field required
        error_messages={'required': 'Please select at least one tag.'}
    )

    class Meta:
        model = Task
        fields = "__all__"
        error_messages = {
            'title': {'required': 'Please enter a title.'},
            'description': {'required': 'Please enter a description.'},
            # Add error messages for other fields as needed
        }
