
from django.db.models import IntegerField
from django.test import TestCase

from kazakhapp.models import *

# Create your tests here.

class YourTestClass(TestCase):
          @classmethod
          def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
                    Artist.objects.create(name='Test', biography='Test bio')
                    pass
          def setUp(self):
        # Setup run before every test method.
                    pass

          def test_name_max_length(self):
                    user = Artist.objects.get(id=1)
                    max_length = user._meta.get_field('name').max_length
                    self.assertEqual(max_length, 200)
                    # self.assertTrue(5==5)
          def test_biography_label(self):
                    user = Artist.objects.get(id=1)
                    field_label = user._meta.get_field('biography').verbose_name
                    self.assertEqual(field_label, 'biography')
          def test_get_absolute_url(self):
                    user = Artist.objects.get(id=1)
                    # This will also fail if the urlconf is not defined.
                    self.assertEqual(user.get_absolute_url(), 'test/fail')
          def test_str_name(self):
                    user = Artist.objects.get(id=1)
                    # This will also fail if the urlconf is not defined.
                    
                    self.assertEqual(user.__str__(), user._meta.get_field('name').value_from_object(user))
          def test_id_type(self):
                    field = Artist._meta.get_field("art_id")
                    self.assertTrue(isinstance(field, IntegerField))
