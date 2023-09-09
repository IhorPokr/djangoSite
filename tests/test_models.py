from django.test import TestCase
from todo_list.models import Tag, Task


class TagModelTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_tag_str_method(self):
        self.assertEqual(str(self.tag), "Test Tag")

    def test_tag_unique_constraint(self):
        with self.assertRaises(Exception) as context:
            Tag.objects.create(name="Test Tag")
        self.assertTrue("UNIQUE constraint failed" in str(context.exception))


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")
        self.task = Task.objects.create(
            content="Test Task",
            is_completed=False,
        )
        self.task.tags.set([self.tag1, self.tag2])

    def test_task_str_method(self):
        expected_str = (
            f"Content: {self.task.content}\n"
            f"Created {self.task.created}\n"
            f"Tags: {', '.join(str(tag) for tag in self.task.tags.all())}"
        )
        self.assertEqual(str(self.task), expected_str)

    def test_task_default_values(self):
        self.assertFalse(self.task.is_completed)
        self.assertIsNone(self.task.deadline)

    def test_task_ordering(self):
        completed_task = Task.objects.create(
            content="Completed Task",
            is_completed=True,
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], completed_task)
        self.assertEqual(tasks[1], self.task)

    def test_task_tags_related_name(self):
        self.assertIn(self.task, self.tag1.tasks.all())
        self.assertIn(self.task, self.tag2.tasks.all())
