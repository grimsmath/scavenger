from django.db import models
from django.utils.timezone import timezone, now
import random

# Create your models here.


def random_string():
    return str(random.randint(1, 4))


class Sheet(models.Model):
    first_name = models.CharField("First Name", max_length=200)
    last_name = models.CharField("Last Name", max_length=200)
    id_number = models.CharField("ID Number",
                                 max_length=8, default='', unique=True)
    sheet_num = models.CharField(
        "Sheet Number", max_length=1, default=random_string())
    start_date = models.DateTimeField(
        "Start Date", default=now, editable=True)
    end_date = models.DateTimeField(
        "End Date", null=True, blank=True)
    icon_found = models.IntegerField("Icons Found", null=True, blank=True)
    clues_solved = models.IntegerField("Clues Solved", null=True, blank=True)

    class Meta:
        verbose_name = "Signup Sheet"
        ordering = ("last_name", "first_name")

    def __str__(self):
        return f"{self.id_number} - {self.last_name}, {self.first_name}"
