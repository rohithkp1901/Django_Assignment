from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class register(models.Model):
    gender_option=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    firstname=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.IntegerField()
    password=models.CharField(max_length=200,null=True,validators=[MinLengthValidator(limit_value=6)])
    gender = models.CharField(max_length=6, choices=gender_option, default='Male')
    def __str__(self):
        return self.firstname
    