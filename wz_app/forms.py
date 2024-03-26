from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Moje_wz

class NewWzForm(forms.ModelForm):
    class Meta:
        model = Moje_wz
        fields = ["Odbiorca", "Numer_samochodu", "Data_dokumentu"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("new-wz-submit",
                   "Add",
                   css_class="rounded-pill mt-4")
        )

class NewWzForm2(forms.ModelForm):
    class Meta:
        model = Moje_wz
        fields = ["Nazwa_produktu", "Numer_produktu", "Ilosc"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("new-wz-submit",
                   "Add",
                   css_class="rounded-pill mt-4")
        )