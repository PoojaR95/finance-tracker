from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    is_default = models.BooleanField(default=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    TYPE_CHOICES = (("income", "Income"), ("expense", "Expense"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    note = models.TextField(blank=True, default="")
    date = models.DateField(default=timezone.localdate)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.type} - {self.amount}"
