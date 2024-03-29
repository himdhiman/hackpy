from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Problem(models.Model):
    difficulty_level = [
        ('1', 'easy'),
        ('2', 'medium'),
        ('3', 'hard')
    ]

    name = models.CharField(max_length = 50)
    description = models.TextField()
    level = models.CharField(max_length = 10, choices = difficulty_level)


    def __str__(self):
        return self.name

class Contest(models.Model):
    name = models.CharField(max_length = 256)
    start_date = models.DateTimeField() #stores with time zone
    end_date = models.DateTimeField()
    description = models.TextField()
    is_private = models.BooleanField(default = False)
    Problems = models.ManyToManyField('Problem')

    def __str__(self):
        return self.name

class StudentContest(models.Model):
    contest = models.ForeignKey('Contest', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.user, self.contest)

class Submission(models.Model):
    LANGUAGES = [
        (1, 'cpp'),
        (2, 'c'),
        (3, 'java'),
        (4, 'python')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    contest = models.ForeignKey('Contest', on_delete = models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete = models.CASCADE)
    source = models.TextField()
    language = models.IntegerField(choices = LANGUAGES)
    score = models.IntegerField(null = True)
    createdAt = models.DateTimeField(auto_now_add = True) #stores the time when the entry is created
