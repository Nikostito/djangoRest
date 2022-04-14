from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@test.com", password="testpass"):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_check(self):
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(
            email, "pass123"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_null_email(self):
        """We raise value error on non emails"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, "pass123"
            )

    def test_create_superuser(self):
        """ Test creating new superuser  """
        user = get_user_model().objects.create_superuser(
            "test@superuser.com",
            "test1234"
        )
        """ Is Superuser is included in PermissionsMixin  """
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag representation """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan",
        )
        self.assertEqual(str(tag), tag.name,)

    def test_ingredient_str(self):
        """Test the ingredient test representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
