from django.test import TestCase
from django.urls import reverse
from catalog.models import Author  # Adjust the import as per your project structure
from django.db import models

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1970-01-01',
            date_of_death='2020-01-01'
        )

    def test_first_name_label(self):
        # Retrieve the field object
        field_label = self.author._meta.get_field('first_name').verbose_name
        # We assume the default label is 'first name' as generated by Django 
        # (fields are turned into verbose names by splitting on underscores and capitalizing).
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        field_label = self.author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        field_label = self.author._meta.get_field('date_of_birth').verbose_name
        # By default, this will be 'date of birth' from the field name.
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        field_label = self.author._meta.get_field('date_of_death').verbose_name
        # This one was explicitly set to 'Died'
        self.assertEqual(field_label, 'Died')

    def test_first_name_max_length(self):
        max_length = self.author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        max_length = self.author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_get_absolute_url(self):
        # The get_absolute_url should return something like `/catalog/author/<id>`
        url = self.author.get_absolute_url()
        # Check that the URL reverses to something valid.
        # reverse('author-detail', args=[str(self.author.id)]) should return the same URL.
        expected_url = reverse('author-detail', args=[str(self.author.id)])
        self.assertEqual(url, expected_url)

    def test_object_str_method(self):
        # __str__ returns 'last_name, first_name'
        expected_object_name = f'{self.author.last_name}, {self.author.first_name}'
        self.assertEqual(str(self.author), expected_object_name)
