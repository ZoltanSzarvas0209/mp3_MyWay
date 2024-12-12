from django.test import TestCase
from .forms import ImageForm
from django.core.exceptions import ValidationError


# Chat GPT was used to troubleshoot
# why testing fails and cloudinary default image set to
# resolve issue
class ImageFormTest(TestCase):
    def test_valid_form(self):
        """Test the form validity with valid Cloudinary data."""
        form_data = {
            'title': 'Sample Image',
            'description': 'This is a sample image description.',
            'image_url': 'placeholder_irkbnr',  # Use Cloudinary asset ID
        }
        form = ImageForm(data=form_data)
        self.assertTrue(form.is_valid())  # Form should be valid

    def test_missing_title(self):
        """Test the form with missing title."""
        form_data = {
            'title': '',  # Missing title
            'description': 'This is a sample image description.',
            'image_url': 'placeholder_irkbnr',
        }
        form = ImageForm(data=form_data)
        self.assertFalse(form.is_valid())  # form is invalid
        self.assertIn('title', form.errors)

    def test_missing_description(self):
        """Test the form with missing description."""
        form_data = {
            'title': 'Sample Image',
            'description': '',  # Missing description
            'image_url': 'placeholder_irkbnr',
        }
        form = ImageForm(data=form_data)
        self.assertFalse(form.is_valid())  # form is invalid
        self.assertIn('description', form.errors)
