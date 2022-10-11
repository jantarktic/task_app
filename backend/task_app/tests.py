from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .models import Task
from .views import TaskView

# Create your tests here.
class ViewSetTest(TestCase):
    def test_view_set(self):
        request = APIRequestFactory().get("")
        task_detail = TaskView.as_view({'get': 'retrieve'})
        task = Task.objects.create(title="Task 6", description="This is a test", due_date=datetime.now())
        response = task_detail(request, pk=task.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], "Overdue")