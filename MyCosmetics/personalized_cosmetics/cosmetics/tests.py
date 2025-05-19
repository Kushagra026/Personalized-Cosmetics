from django.test import TestCase
from .forms import YourForm  # Replace with your actual form class
from .models import YourModel  # Replace with your actual model class

class YourFormTest(TestCase):
    def test_form_valid(self):
        form_data = {
            'field1': 'value1',  # Replace with actual field names and values
            'field2': 'value2',
        }
        form = YourForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            'field1': '',  # Invalid data for required field
            'field2': 'value2',
        }
        form = YourForm(data=form_data)
        self.assertFalse(form.is_valid())

class YourModelTest(TestCase):
    def setUp(self):
        YourModel.objects.create(field1='value1', field2='value2')  # Replace with actual fields

    def test_model_str(self):
        obj = YourModel.objects.get(field1='value1')
        self.assertEqual(str(obj), 'Expected String Representation')  # Replace with expected output