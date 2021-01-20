from django.db import models

class Exam(models.Model):
    Question = models.TextField()
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    CorrectAnswer = models.CharField(max_length=100)
    examcompleted = models.DateTimeField(null=True, blank=True)
    Explanation = models.TextField()
    def __str__(self):
        return self.Question
