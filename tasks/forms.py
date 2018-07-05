from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    """
    A model form for a Task object.
    """
    class Meta:
        exclude = ['pk', 'owner', 'complete_time']
        model = Task
