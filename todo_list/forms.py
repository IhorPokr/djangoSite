from django import forms
from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Check if there are any tags in the database, if not, display a message.
        if not Tag.objects.exists():
            self.fields['tags'].queryset = Tag.objects.none()
            self.fields['tags'].help_text = 'No tags available. Please create a tag first.'

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
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
