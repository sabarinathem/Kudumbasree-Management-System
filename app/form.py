from django.forms import ModelForm
from app.models import Savings,Member
from django.forms import widgets
from django.forms import fields
class SavingForm(ModelForm):
    class Meta:
        model=Savings
        fields=('first_weak','second_weak','third_weak','fourth_weak','fifth_weak')

class MemberForm(ModelForm):
    class Meta:
        model=Member
        fields=('name','member_number','date_of_membership','category')
        widgets={
            'date_of_membership':widgets.DateInput(attrs={'type':'date'}),
            
        }