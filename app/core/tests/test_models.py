from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'test@google.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that email for a new user is normalized"""

        email = "test@GOOGLE.COM"
        user = get_user_model().objects.create_user(email, 'Test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raised error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new super-user"""

        user = get_user_model().objects.create_superuser(
            'test@google.com',
            'TestPassw123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
