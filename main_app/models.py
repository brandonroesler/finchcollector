from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('R', 'Rodents'),
    ('F', 'Fish'),
    ('T', 'Trash')
)

class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

    def get_absolute_url(self):
        return reverse('languages_detail', kwargs={'pk': self.id})

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']