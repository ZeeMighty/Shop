from django import forms
from .models import Good_Get, Good

class GoodGet(forms.ModelForm):
    class Meta:
        model = Good_Get
        Size = forms.ModelChoiceField(to_field_name = 'Size', queryset = Good.objects.all())
        fields = '__all__'
