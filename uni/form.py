from django.forms import *
from uni.models import *


class StudentForm(ModelForm):
    class Meta:
        model = Studierende
        exclude = ()
        labels = {'firstN': 'First Name',
                  'lastN': 'Last Name' , }