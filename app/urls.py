from django.urls import path
from app import views

app_name='app'
urlpatterns=[

    path('',views.index,name="index"),
    path('<int:id>/select_month_and_year',views.select_month_and_year,name="select_month_and_year"),
    path('<int:id>/add_or_update_savings',views.add_or_update_savings,name="add_or_update_savings"),
    path('<int:id>/save',views.save,name="save"),
    path('show/',views.show,name="show"),
    path('savings_of_intended_month/',views.savings_of_intended_month,name="savings_of_intended_month")
]