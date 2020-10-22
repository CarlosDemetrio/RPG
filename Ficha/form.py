from django.forms import ModelForm
from .models import Ficha


class FichaForm(ModelForm):
    class Meta:
        model = Ficha
        fields = '__all__'
