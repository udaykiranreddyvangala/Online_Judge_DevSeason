from django import forms;
from .models import CodeSubmission

Language_Choices=[
    ("py","Python"),
    ("c","C"),
    ("cpp","C++"),
]
class CodeSubmissionForm(forms.ModelForm):
    language=forms.ChoiceField(choices=Language_Choices)
    
    class Meta:
        model=CodeSubmission
        fields=["language","code","input_data"]