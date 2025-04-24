from django import forms
from .models import Parts


class PartsForm(forms.ModelForm):
    class Meta:
        model = Parts
        exclude = ['product']

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
        product = self.product or getattr(self.instance, 'product', None)

        if product:
            category = product.category.name
            category_fields = {
                'Motherboard': ['socket_mb2cpu', 'socket_mb2gpu', 'socket_mb2ssd', 'socket_mb2ram', 'socket_mb2psu', 'chipset', 'usb_ports', 'model_series'],
                'GPU': ['socket_mb2gpu', 'frequency', 'recommended_power_supply', 'model_series'],
                'SSD': ['socket_mb2ssd', 'memory_size', 'model_series'],
                'RAM': ['socket_mb2ram', 'memory_size', 'model_series'],
                'PSU': ['socket_mb2psu', 'psu_power', 'model_series'],
                'Processors': ['socket_mb2cpu', 'frequency', 'recommended_power_supply', 'model_series'],
            }
            allowed_fields = category_fields.get(category, [])

            for field in list(self.fields):
                if field not in allowed_fields:
                    self.fields.pop(field)
