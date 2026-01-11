from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient, OPVisit, IPAdmission, BillingQueue, Billing
from .serializers import (
    PatientSerializer, OPVisitSerializer,
    IPAdmissionSerializer, BillingSerializer
)


@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        patient = serializer.save()

        # Auto queue number
        last = BillingQueue.objects.order_by('-queue_number').first()
        queue_no = 1 if not last else last.queue_number + 1

        BillingQueue.objects.create(
            patient=patient,
            patient_type=patient.patient_type,
            queue_number=queue_no
        )

        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def create_op_visit(request):
    serializer = OPVisitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def create_ip_admission(request):
    serializer = IPAdmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def do_billing(request):
    serializer = BillingSerializer(data=request.data)
    if serializer.is_valid():
        billing = serializer.save()
        BillingQueue.objects.filter(patient=billing.patient).update(status='Paid')
        return Response(serializer.data)
    return Response(serializer.errors)
