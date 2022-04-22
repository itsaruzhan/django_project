from django.test import TestCase
from django.template.defaultfilters import slugify
from polls.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
     
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author.first_name
        self.assertEqual(field_label, 'Big')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)
  
    
    def test_post_has_slug(self):
        author = Author.objects.get(id=1)
        author.save()
        self.assertEqual(author.slug, slugify(author.first_name))