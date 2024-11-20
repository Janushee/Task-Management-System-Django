from django.db import models

from employee.models import Employee

# specifying choices

STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("In_Progress", "In_Progress"),
    ("Completed", "Completed"),
)


PRIORITY_CHOICES = (
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
)
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = 'Pending'
        )
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY_CHOICES,
        default = 'Low'
        )
    due_date = models.DateField()
    assigned_to = models.ForeignKey(Employee,related_name='task', on_delete=models.CASCADE)
    parent_task = models.ForeignKey('self',null=True,related_name='subtasks', blank=True, on_delete=models.CASCADE)

