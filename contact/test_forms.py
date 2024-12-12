from django.test import TestCase
from .models import Contact
from .forms import Contact_form


class ContactFormTest(TestCase):
    def test_valid_form(self):
        """Test the form with valid data."""
        form_data = {
            'title': 'Test Title',
            'content': 'This is a test message content.'
        }
        form = Contact_form(data=form_data)

        # Check that the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_title(self):
        """Test the form with missing title."""
        form_data = {
            'content': 'This is a test message content.'
        }
        form = Contact_form(data=form_data)

        self.assertFalse(form.is_valid())  # form not valid
        self.assertIn('title', form.errors)

    def test_invalid_form_missing_content(self):
        """Test the form with missing description."""
        form_data = {
            'title': 'Test Title'
        }
        form = Contact_form(data=form_data)
        
        self.assertFalse(form.is_valid())  # form not valid
        self.assertIn('content', form.errors)
