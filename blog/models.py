from django.db import models

# Create your models here.


class Entry(models.Model):
    header = models.CharField(max_length=120)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("Author", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.author) + " ----- " + self.header


class Author(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120, default=" ")
    born_date = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name + " " + self.surname



