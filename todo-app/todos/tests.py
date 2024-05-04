from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo

class TodoModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password='password')
        Todo.objects.create(
            title="Test Todo",
            created_by=self.user,
        )
    
    def test_todo_created(self):
        todo = Todo.objects.get(title="Test Todo")
        self.assertEqual(todo.title, "Test Todo")