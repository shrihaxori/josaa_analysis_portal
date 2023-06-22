from django.db import models

# Create your models here.
class College(models.Model):
    program_name = models.CharField(max_length=200)
    seat_type = models.BooleanField()
    quota = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    opening_rank = models.PositiveIntegerField(default=200000)
    closing_rank = models.PositiveIntegerField(default=200000)
    year = models.PositiveSmallIntegerField(default = 2022)
    round = models.PositiveSmallIntegerField(default = 6)
    def __str__(self):
        return self.college_text

class User(models.Model):
    mains_rank = models.IntegerField()
    advanced_rank = models.IntegerField()
    seat_type = models.BooleanField()
    quota = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    def __str__(self):
        return self.user_text