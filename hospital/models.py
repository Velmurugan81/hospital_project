from django.db import models
from django.utils import timezone


# =========================
# 1. Patient (Reception)
# =========================
class Patient(models.Model):
    PATIENT_TYPE_CHOICES = (
        ('OP', 'Out Patient'),
        ('IP', 'In Patient'),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    patient_type = models.CharField(max_length=2, choices=PATIENT_TYPE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# =========================
# 2. OP Workflow
# =========================
class OPVisit(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    visit_date = models.DateField(default=timezone.now)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"OP - {self.patient.name}"


# =========================
# 3. IP Workflow
# =========================
class IPAdmission(models.Model):
    STATUS_CHOICES = (
        ('Admitted', 'Admitted'),
        ('Discharged', 'Discharged'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=10)
    admission_date = models.DateField(default=timezone.now)
    discharge_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Admitted')

    def __str__(self):
        return f"IP - {self.patient.name}"


# =========================
# 4. Lab Tests
# =========================
class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.test_name} - {self.patient.name}"


# =========================
# 5. Pharmacy
# =========================
class PharmacyBill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.medicine_name} - {self.patient.name}"


# =========================
# 6. Billing Queue
# =========================
class BillingQueue(models.Model):
    QUEUE_STATUS_CHOICES = (
        ('Waiting', 'Waiting'),
        ('Processing', 'Processing'),
        ('Paid', 'Paid'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient_type = models.CharField(max_length=2)  # OP / IP
    queue_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=QUEUE_STATUS_CHOICES, default='Waiting')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['queue_number']

    def __str__(self):
        return f"Queue {self.queue_number} - {self.patient.name}"


# =========================
# 7. Final Billing
# =========================
class Billing(models.Model):
    PAYMENT_MODE_CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES)
    bill_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='Paid')

    def __str__(self):
        return f"Bill - {self.patient.name}"
