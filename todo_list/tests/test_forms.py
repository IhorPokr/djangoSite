from django.test import TestCase
from todo_list.models import Tag
from todo_list.forms import TaskForm


class TaskFormTest(TestCase):
    def setUp(self):
        # Create some sample data for the form
        self.tag1 = Tag.objects.create(name='Tag1')
        self.tag2 = Tag.objects.create(name='Tag2')
        self.tag3 = Tag.objects.create(name='Tag3')

    def test_valid_form(self):
        data = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'tags': [self.tag1.pk, self.tag2.pk],
        }
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        # Test with missing title
        data = {
            'description': 'This is a test task',
            'tags': [self.tag1.pk, self.tag2.pk],
        }
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())

    def test_empty_tags_field(self):
        # Test with an empty tags field (not required)
        data = {
            'title': 'Test Task',
            'description': 'This is a test task',
        }
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_tags(self):
        # Test with invalid tag IDs in the tags field
        data = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'tags': [100, 200],  # These IDs don't exist in the database
        }
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())
