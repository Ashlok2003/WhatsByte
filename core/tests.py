from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient, Doctor, PatientDoctorMapping

User = get_user_model()

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(email='test@example.com', name='Test User', password='pass123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('pass123'))

class PatientModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', name='Test User', password='pass123')

    def test_patient_creation(self):
        patient = Patient.objects.create(
            name='Ashlok Chaudhary',
            age=22,
            gender='Male',
            address='Virar, Mumbai, Maharashtra',
            created_by=self.user
        )
        self.assertEqual(patient.name, 'Ashlok Chaudhary')
        self.assertEqual(patient.created_by, self.user)


