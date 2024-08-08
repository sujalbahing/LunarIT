from django.db import models
from django.contrib.auth.models import User
from home.models import Course


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=100)
    purchase_order_id = models.CharField(max_length=255, unique=True)
    
    def _str_(self):
        return self.user.username
    
