from django.urls import path
from .views import get_zaproz,get_detail,create_person,delete_person,update_person

urlpatterns=[
    path('all_persons/',get_zaproz),
    path('one_person/<int:pk>/',get_detail),
    path('person_create/',create_person),
    path('person_delete/<int:pk>/', delete_person),
    path('person_update/<int:pk>/',update_person)
]