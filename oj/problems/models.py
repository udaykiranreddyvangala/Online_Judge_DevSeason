from django.db import models

# Create your models here.
class problem(models.Model):
    problem_name=models.CharField(max_length=50)
    problem_statement=models.CharField(max_length=500)
    level=models.CharField(max_length=10,null=True)
    
class TestCase(models.Model):
    problem=models.ForeignKey(problem,on_delete=models.CASCADE)
    input=models.FileField()
    output=models.FileField()
    