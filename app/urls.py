from django.urls import path
from app import views

app_name='app'
urlpatterns=[

    path('',views.index,name="index"),
    path('<int:id>/select_month_and_year',views.select_month_and_year,name="select_month_and_year"),
]