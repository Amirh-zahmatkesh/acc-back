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
            slug='fanancial-accounting',
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

    def test_category_str(self):
        """Test the category string representation without a parent"""
        category = models.Category.objects.create(
            name='financial accounting',
            slug='financial accounting'
        )
        self.assertEqual(str(category), category.name)

    def test_category_str_with_parent(self):
        """Test the category string representation with parent"""
        category1 = models.Category.objects.create(
            name='accounting',
            slug='accounting'
        )
        category2 = models.Category.objects.create(
            name='financial accounting',
            slug='financial-accounting',
            parent=category1
        )
        self.assertEqual(str(category2),
                         f"{category1.name} -> {category2.name}")

    def test_keyword_str(self):
        """Test the keyword string representation"""
        keyword = models.Keyword.objects.create(word='keyword')

        self.assertEqual(str(keyword), keyword.word)
