from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Commtype(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique = True)
    url = models.CharField(max_length=20, unique = True, validators=[RegexValidator(regex="^[a-zA-Z0-9_\-]+$", message="Only alphanumeric, dashes, and underscores allowed")])
    rank = models.IntegerField(default=1)
    is_middle = models.BooleanField(default=False)
    committees = models.ManyToManyField("Techmuncommittee", related_name="commtype", null=True, blank = True)
    def __str__(self):
        return self.name


class Techmuncommittee(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique = True)
    url = models.CharField(max_length=20, unique = True, validators=[RegexValidator(regex="^[a-zA-Z0-9_\-]+$", message="Only alphanumeric, dashes, and underscores allowed")])
    style = models.CharField(max_length=40, null = True)
    is_crisis = models.BooleanField(default=False)
    is_middleschool = models.BooleanField(default=False)

    topic1 = models.CharField(max_length=100, default = "Topic 1 coming soon!")
    topic2 = models.CharField(max_length=100, default = "Topic 2 coming soon!")
    chairs = models.ManyToManyField("Chair", related_name="committee", null = True, blank = True)
    image = models.ImageField(upload_to = "techmun_photos/", null = True, blank = True)
    background_guide = models.FileField(upload_to="background_guides/", null = True, blank = True)
    def __str__(self):
        return self.name


class Chair(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique = True)
    biography = models.TextField(max_length=5000, default="Biography coming soon!")  
    is_director = models.BooleanField(default= False)
    image = models.ImageField(upload_to = "chair_photos/", null = True, blank = True)
  
    def __str__(self):
        return self.name