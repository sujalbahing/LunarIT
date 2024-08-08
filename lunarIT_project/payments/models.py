from django.db import models
from django.contrib.auth.models import User
from home.models import Course

# class Payment(models.Model):
#     STATUS_CHOICES = (
#         ('PENDING', 'Pending'),
#         ('COMPLETED', 'Completed'),
#         ('FAILED', 'Failed'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
#     transaction_id = models.CharField(max_length=50, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user} - {self.amount} - {self.status}"
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=100)
    purchase_order_id = models.CharField(max_length=255, unique=True)
    
    def _str_(self):
        return self.user.username