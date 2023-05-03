from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from ..serializers import UserSerializer, PatientSerializer
from ..models import Patient


class UserSerializerTest(APITestCase):

    def test_create_user(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User'
        }
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, user_data['username'])
        self.assertEqual(user.email, user_data['email'])
        self.assertEqual(user.first_name, user_data['first_name'])
        self.assertEqual(user.last_name, user_data['last_name'])


class PatientSerializerTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        self.patient = Patient.objects.create(
            user=self.user,
            age=30,
            weight_kg=70.00,
            height_m=1.75
        )

    def test_create_patient(self):
        patient_data = {
            'user': {
                'username': 'newpatient',
                'email': 'newpatient@example.com',
                'password': 'newpassword',
                'first_name': 'New',
                'last_name': 'Patient'
            },
            'age': 25,
            'weight_kg': 60.00,
            'height_m': 1.65
        }
        serializer = PatientSerializer(data=patient_data)
        self.assertTrue(serializer.is_valid())
        patient = serializer.save()
        self.assertEqual(patient.user.username,
                         patient_data['user']['username'])
        self.assertEqual(patient.user.email, patient_data['user']['email'])
        self.assertEqual(patient.age, patient_data['age'])
        self.assertEqual(float(patient.weight_kg), patient_data['weight_kg'])
        self.assertEqual(float(patient.height_m), patient_data['height_m'])

    def test_update_patient(self):
        updated_data = {
            'user': {
                'username': 'updateduser',
                'email': 'updateduser@example.com',
                'password': 'updatedpassword',
                'first_name': 'Updated',
                'last_name': 'User'
            },
            'age': 35,
            'weight_kg': 75.00,
            'height_m': 1.80
        }
        serializer = PatientSerializer(
            instance=self.patient, data=updated_data, partial=True)
        self.assertTrue(serializer.is_valid())
        patient = serializer.save()
        self.assertEqual(patient.user.username,
                         updated_data['user']['username'])
        self.assertEqual(patient.user.email, updated_data['user']['email'])
        self.assertEqual(patient.age, updated_data['age'])
        self.assertEqual(float(patient.weight_kg), updated_data['weight_kg'])
        self.assertEqual(float(patient.height_m), updated_data['height_m'])
