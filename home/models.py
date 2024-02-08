from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName= models.CharField(max_length=122)
    lastName=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phoneNo=models.CharField(max_length=122)
    message=models.TextField()

    def __str__(self):
        return self.firstName