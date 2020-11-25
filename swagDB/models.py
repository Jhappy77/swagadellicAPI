from django.db import models

# The id fields are created automatically by Django, except for ticket, which is done manually.

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    release_date = models.DateField('release date')
    length = models.IntegerField(default=90)

class Theatre(models.Model):
    theatre_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

class Screening(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screening_time = models.DateTimeField('start time')
    #SEAT MAP TYPE will be included here in the future

class RegisteredUser(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField('birthday')
    password = models.CharField(max_length = 200)
    email = models.EmailField()

class Ticket(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=75)
    seat_no = models.IntegerField()
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
    user_id = models.ForeignKey(RegisteredUser, on_delete=models.SET_NULL, null=True, blank=True, default = None)

class Payment(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    user_id = models.ForeignKey(RegisteredUser, on_delete=models.SET_NULL, null=True, blank=True, default = None)
