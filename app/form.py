from django.forms import ModelForm
from app.models import Savings
class SavingForm(ModelForm):
    class Meta:
        model=Savings
        fields=('first_weak','second_weak','third_weak','fourth_weak','fifth_weak')