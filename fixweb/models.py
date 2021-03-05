from django.db import models

# Create your models here.
class Contact(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=8)
    message = models.TextField(max_length=30)

    def __str__(self):
        return self.first + " , " + self.last + " , " + self.email + " , " + self.phone + " , " + self.message