from django.test import TestCase
from django.urls import reverse
from todo_list.models import Tag, Task


class TestViews(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task Content")

    def test_home_page_view(self):
        response = self.client.get(reverse("catalog:home-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/home_page.html")

    def test_task_create_view(self):
        response = self.client.get(reverse("catalog:task-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_update_view(self):
        response = self.client.get(reverse("catalog:task-update", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_delete_view(self):
        response = self.client.get(reverse("catalog:task-delete", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_confirm_delete.html")

    def test_tag_list_view(self):
        response = self.client.get(reverse("catalog:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tags_list.html")

    def test_tag_create_view(self):
        response = self.client.get(reverse("catalog:tag-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_form.html")

    def test_tag_update_view(self):
        response = self.client.get(reverse("catalog:tag-update", args=[self.tag.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_form.html")

    def test_tag_delete_view(self):
        response = self.client.get(reverse("catalog:tag-delete", args=[self.tag.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_confirm_delete.html")

    def test_toggle_assign_to_task_view(self):
        initial_is_completed = self.task.is_completed
        response = self.client.post(reverse("catalog:toggle-task-assign", args=[self.task.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        updated_task = Task.objects.get(id=self.task.id)
        self.assertNotEqual(initial_is_completed, updated_task.is_completed)
