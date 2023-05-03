from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Patient


class PatientModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='test_password')

    def test_create_patient_instance(self):
        patient = self.make_patient()
        patient.full_clean()
        patient.save()
        self.assertEqual(str(patient), 'John Doe')

    def test_invalid_age(self):
        with self.assertRaises(ValidationError):
            patient = self.make_patient(age=151)
            patient.full_clean()

    def test_invalid_weight_kg(self):
        with self.assertRaises(ValidationError):
            patient = self.make_patient(weight_kg=0)
            patient.full_clean()

    def test_invalid_height_m(self):
        with self.assertRaises(ValidationError):
            patient = self.make_patient(height_m=0)
            patient.full_clean()

    def make_patient(self,
                     age=30,
                     weight_kg=70.0,
                     height_m=1.75
                     ):

        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            email='johndoe@example.com',
            password='test_password'
        )

        return Patient.objects.create(
            user=user,
            age=age,
            weight_kg=weight_kg,
            height_m=height_m
        )
