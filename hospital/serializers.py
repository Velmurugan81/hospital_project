from rest_framework import serializers
from .models import Patient, OPVisit, IPAdmission, BillingQueue, Billing


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class OPVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPVisit
        fields = '__all__'


class IPAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAdmission
        fields = '__all__'


class BillingQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingQueue
        fields = '__all__'


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'
