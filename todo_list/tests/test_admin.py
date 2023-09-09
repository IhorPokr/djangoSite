from django.test import TestCase
from django.contrib.auth.models import User
from todo_list.models import Task, Tag


class AdminPanelTestCase(TestCase):
    def setUp(self):
        # Create a superuser for logging into the admin panel
        self.admin_user = User.objects.create_superuser(
            username='admin', password='admin_password', email='admin@example.com'
        )

        # Create some tags
        self.tag1 = Tag.objects.create(name='Tag 1')
        self.tag2 = Tag.objects.create(name='Tag 2')

        # Create some tasks with tags
        self.task1 = Task.objects.create(content='Task 1')
        self.task1.tags.set([self.tag1])

        self.task2 = Task.objects.create(content='Task 2')
        self.task2.tags.set([self.tag2])

    def test_task_admin_search(self):
        # Log in as the admin user
        self.client.login(username='admin', password='admin_password')

        # Perform a search for "Task 1"
        response = self.client.get('/admin/todo_list/task/?q=Task+1')

        # Check if the search result contains the task
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

    def test_task_admin_filter(self):
        # Log in as the admin user
        self.client.login(username='admin', password='admin_password')

        # Filter tasks by Tag 1
        response = self.client.get('/admin/todo_list/task/', {'tags__id__exact': self.tag1.id})

        # Check if the filtered result contains Task 1 and not Task 2
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

    def test_tag_admin(self):
        # Log in as the admin user
        self.client.login(username='admin', password='admin_password')

        # Access the Tag admin page
        response = self.client.get('/admin/todo_list/tag/')

        # Check if the tags are displayed in the admin panel
        self.assertContains(response, 'Tag 1')
        self.assertContains(response, 'Tag 2')
