from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='students/',null=True,blank=True)
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
        ],
        default='Male'
    )
    age = models.IntegerField()
    email = models.EmailField()
    date = models.DateField(default='2021-02-21')


    def __str__(self):
        return self.name
class Exam(models.Model):
    name = models.CharField(max_length=20)
    exam_code = models.IntegerField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name