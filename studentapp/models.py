from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name}"

class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city_name}"

class Student(models.Model):
    Student_name = models.CharField(max_length=50)
    Student_phone = models.BigIntegerField()
    Student_email = models.CharField(max_length=100)
    Student_city = models.ForeignKey(City, on_delete=models.CASCADE)
    Student_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Student_fees = models.IntegerField()

