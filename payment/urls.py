from django.urls import path
from . import views

app_name ='payment'

urlpatterns = [
    path('pay/', views.payment_process, name='process'),
    path('callback/', views.payment_response, name='response')
]
