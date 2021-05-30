from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120, default=" ")
    degree = models.CharField(max_length=120, null=True, blank=True, default="Prof. Dr.")
    image = models.ImageField()

    def get_full_name(self):
        if self.degree:
            return self.degree + " " + self.name + " " + self.surname
        else:
            return self.name + " " + self.surname

    def __str__(self):
        return self.get_full_name()


class BoardMember(Person):
    year = models.ForeignKey("Year", null=True, blank=True, on_delete=SET_NULL)
    role = models.ForeignKey("Role", null=True, blank=True, on_delete=SET_NULL)

    def __str__(self):
        return str(self.year) + " ----- " + self.get_full_name()

class Advisor(Person):
    school = models.CharField(max_length=120)
    
    def __str__(self):
        return self.school + " --- " + self.get_full_name()


class Year(models.Model):
    year = models.PositiveSmallIntegerField(default=2021)

    def __str__(self):
        return str(self.year)

class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role

