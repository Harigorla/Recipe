from django.forms import ModelForm
from .models import MenuName


class MenuForm(ModelForm):
    class Meta:
        model = MenuName
        fields = "__all__"
