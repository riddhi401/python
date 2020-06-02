from django import forms
from .models import student


class StudentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ('fullname','mobile','rollnumber','div')
        labels = {
            'fullname':'Full Name',
            'rollnumber':'Roll Number'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['div'].empty_label = "Select"
        self.fields['rollnumber'].required = False
