from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_certificate_str(self):
        """Test the certificate string representation"""
        certificate = models.Certificate.objects.create(
            name='financial accounting',
            minimum_grade=85,
            user=get_user_model().objects.create_user(
                email='testuser@gmail.com',
                password='testpass'
            )
        )

        self.assertEqual(str(certificate), certificate.name)

    @patch('uuid.uuid4')
    def test_certificate_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the currect location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.certificate_image_file_path(None, 'my_image.jpg')

        expected_path = f'uploads/certificateimages/{uuid}.jpg'

        self.assertEqual(file_path, expected_path)
