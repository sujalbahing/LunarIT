from django.db import models

class Course(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Name")
    Image = models.ImageField(upload_to='images/', blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    Description = models.TextField(max_length=100, verbose_name="Description")
    
    def __str__(self):
       return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Name")
    Image = models.ImageField(upload_to='images/', blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    Description = models.TextField(max_length=100, verbose_name="Description")
    
class Contact(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Name")
    Email = models.EmailField(verbose_name="Email")
    Subject = models.CharField(max_length=100, verbose_name="Subject")
    Phone = models.CharField(max_length=15, verbose_name="Phone")
    Message = models.TextField(verbose_name="Message")
    
    def __str__(self):
       return self.Name