from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Year(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique = True)
    url = models.CharField(max_length=20, unique = True, validators=[RegexValidator(regex="^[a-zA-Z0-9_\-]+$", message="Only alphanumeric, dashes, and underscores allowed")])
    image = models.ImageField(upload_to = "year_photos/", null = True, blank = True)

    conferences = models.ManyToManyField("Conference", related_name="year")

    def __str__(self):
        return self.name

class Conference(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique = True)
    url = models.CharField(max_length=20, unique = True, validators=[RegexValidator(regex="^[a-zA-Z0-9_\-]+$", message="Only alphanumeric, dashes, and underscores allowed")])
    image = models.ImageField(upload_to = "award_photos/", null = True, blank = True)

    committees = models.ManyToManyField("Committee", related_name="conference")
    delegationaward = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return self.name

class Committee(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)

    delegations = models.ManyToManyField("Delegation", related_name="committee")

    def __str__(self):
        return self.name

class Delegation(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    gavel = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    def amir(self):
        if name == "Amir Alkateb":
            gavel = "Honorable Mention"

