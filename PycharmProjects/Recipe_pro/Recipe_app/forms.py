from django.forms import ModelForm
from .models import NameList


class NameForm(ModelForm):

    class Meta:
        model = NameList
        fields = '__all__'
