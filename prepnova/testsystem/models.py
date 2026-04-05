from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('python', 'Python'),
    ('django', 'Django'),
    ('drf', 'DRF'),
    ('sql', 'SQL'),
    ('mysql', 'MySQL'),
    ('web', 'Web Development'),
    ('ai_ds', 'AI & Data Science'),
    ('ai_da', 'AI Data Analyst'),
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('database', 'Database'),
]

DIFFICULTY_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]

class Test(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()
    option1 = models.CharField(max_length=255, blank=True, null=True)
    option2 = models.CharField(max_length=255, blank=True, null=True)
    option3 = models.CharField(max_length=255, blank=True, null=True)
    option4 = models.CharField(max_length=255, blank=True, null=True)
    correct_answer = models.CharField(max_length=255)
    explanation = models.TextField()

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
