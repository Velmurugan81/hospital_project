from django.urls import path
from .views import (
    create_patient,
    create_op_visit,
    create_ip_admission,
    do_billing
)

urlpatterns = [
    path('patient/create/', create_patient),
    path('op/create/', create_op_visit),
    path('ip/create/', create_ip_admission),
    path('billing/pay/', do_billing),
]
