from django.forms import ModelForm
from .models import Repair


class RepairForm(ModelForm):
    class Meta:
        model = Repair
        fields = ['type_of_repair', 'my_image', 'description', 'price_link']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})

