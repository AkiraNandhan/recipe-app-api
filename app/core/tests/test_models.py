from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email='test@londonappdevloper.com'
        password='Testpass123'
        user=get_user_model().objects.create_user(
        email=email,
        password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalozed"""
        email='test@LONDONAPPDEV.COM'
        user=get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())


    def test_new_user_invalid_email(self):
        """test creating a user with no email raises errors"""
        with self.assertRaises(ValueError):
            user=get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        """testing create the new super user"""
        user=get_user_model().objects.create_superuser(
        'test@londonappdevloper.com',
        'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
