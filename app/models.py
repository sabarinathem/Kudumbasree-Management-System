from django.db import models

# Create your models here.

class Member(models.Model):

    name=models.CharField(max_length=100,null=True,blank=True)
    member_number=models.IntegerField(null=True,blank=True)
    date_of_membership=models.DateField(null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    signature=models.ImageField(null=True,blank=True,upload_to="signature/")
    image=models.ImageField(null=True,blank=True,upload_to="image/")

    def __str__(self):
        return (self.name)

class Savings(models.Model):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    month=models.CharField(max_length=100,null=True,blank=True)
    year=models.CharField(max_length=100,null=True,blank=True)
    previous_month_balance=models.IntegerField(null=True,blank=True)
    first_weak=models.IntegerField(null=True,blank=True)
    second_weak=models.IntegerField(null=True,blank=True)
    third_weak=models.IntegerField(null=True,blank=True)
    fourth_weak=models.IntegerField(null=True,blank=True)
    fifth_weak=models.IntegerField(null=True,blank=True)
    savings_of_this_month=models.IntegerField(null=True,blank=True)
    total_savings=models.IntegerField(null=True,blank=True)