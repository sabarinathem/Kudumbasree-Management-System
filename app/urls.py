from os import name
from django.urls import path
from app import views
from django.views.generic import TemplateView
app_name='app'
urlpatterns=[

    path('',views.startpage,name="startpage"),
    path('main/',TemplateView.as_view(template_name="app/main.html")),
    path('index/',views.index,name="index"),
    path('addmember/',views.add_member,name="add_member"),
    path('<int:id>/select_month_and_year',views.select_month_and_year,name="select_month_and_year"),
    path('<int:id>/add_or_update_savings',views.add_or_update_savings,name="add_or_update_savings"),
    path('<int:id>/save',views.save,name="save"),
    path('show/',views.show,name="show"),
    path('savings_of_intended_month/',views.savings_of_intended_month,name="savings_of_intended_month"),
]