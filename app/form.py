from django.forms import ModelForm
from app.models import Savings,Member
from django.forms import widgets
from django.forms import fields
class SavingForm(ModelForm):
    class Meta:
        model=Savings
        fields=('first_weak','second_weak','third_weak','fourth_weak','fifth_weak')
        widgets={
            'first_weak':widgets.NumberInput(attrs={'class':'form-control','placeholder':'ഒന്നാം ആഴ്ച'}),
            'second_weak':widgets.NumberInput(attrs={'class':'form-control','placeholder':'രണ്ടാം ആഴ്ച'}),
            'third_weak':widgets.NumberInput(attrs={'class':'form-control','placeholder':'മൂന്നാം ആഴ്ച'}),
            'fourth_weak':widgets.NumberInput(attrs={'class':'form-control','placeholder':'നാലാം ആഴ്ച'}),
            'fifth_weak':widgets.NumberInput(attrs={'class':'form-control','placeholder':'അഞ്ചാം ആഴ്ച'}),
        }

class MemberForm(ModelForm):
    class Meta:
        model=Member
        fields=('name','member_number','date_of_membership','category')
        widgets={
            'date_of_membership':widgets.DateInput(attrs={'type':'date'}),
            
        }