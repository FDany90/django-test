from django.urls import path
from basicapp import views

#TEMPLA TAGGINNG

app_name = 'basicapp'

urlpatterns=[

    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
]
