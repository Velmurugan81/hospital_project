from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(OPVisit)
admin.site.register(IPAdmission)
admin.site.register(LabTest)
admin.site.register(PharmacyBill)
admin.site.register(BillingQueue)
admin.site.register(Billing)

