from django import forms
from batteries.models import Battery
# from django.core.exceptions import ValidationError

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


class BatteryForm(forms.models.ModelForm):

    class Meta:
        model = Battery
        fields = ('cells', 'capacity', 'nickname', 'barcode', 'cell_voltage')
        widgets = {
            'cells': forms.fields.IntegerField(),
            'capacity': forms.fields.IntegerField(),
            'nickname': forms.fields.TextInput(),
            'barcode' : forms.fields.TextInput(),
            'cell_voltage' : forms.fields.DecimalField(),
            #'text': forms.fields.TextInput(attrs={
            #   'placeholder': 'Enter a to-do item',
            #   'class': 'form-control input-lg',
            #}),
        }
        error_messages = {
            #'text': {'required': EMPTY_ITEM_ERROR}
        }

    def save(self, for_user):
        self.instance.user = for_user
        return super().save()
