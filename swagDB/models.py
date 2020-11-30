from django.db import models

# The id fields are created automatically by Django, except for ticket, which is done manually.

class Movie(models.Model):

    ACTION = "Action"

    GENRE_TYPE_CHOICES = (
        ("Horror", 'Horror'),
        (ACTION, 'Action'),
        ("Comedy", 'Comedy'),
        ("Romance", 'Romance'),
        ("Thriller", 'Thriller'),
        ("Drama", 'Drama'),
        ("Scifi", 'Scifi'),
        ("Nonfic", 'Non Fiction'),
    )

    movie_name = models.CharField(max_length=250)
    genre = models.CharField(
        max_length=20,
        choices = GENRE_TYPE_CHOICES,
        default = ACTION
    )
    release_date = models.DateField('release date')
    length = models.IntegerField(default=90)
    image_link = models.URLField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return self.movie_name + " (Id = " + str(self.id) + ")"

class Theatre(models.Model):
    LARGE = 'LRG'  #30 columns 20 rows
    TINY = 'TNY' # 10 columns 5 rows
    SMALL = 'SML' # 20 columns 15 rows
    HUGE = 'HUG' # 40 columns 25 rows

    THEATRE_TYPE_CHOICES = (
        (LARGE, 'Large 20x30'),
        (TINY, 'Tiny 5x10'),
        (SMALL, 'Small 15x20'),
        (HUGE, 'Huge 25x40')
    )

    theatre_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    theatre_type = models.CharField(
        max_length=3,
        choices=THEATRE_TYPE_CHOICES,
        default = LARGE
    )

    def __str__(self):
        return self.theatre_name + " (Id = " + str(self.id) + ")"

class Screening(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screening_time = models.DateTimeField('start time')
    #SEAT MAP TYPE will be included here in the future
    def __str__(self):
        return str(self.movie_id.movie_name) + " @"  + str(self.theatre_id.theatre_name) + " @ " + self.screening_time.strftime("%m/%d %H:%M") #strftime(self.screening_time)


class RegisteredUser(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField('birthday')
    password = models.CharField(max_length = 200)
    email = models.EmailField(primary_key=True)

class Ticket(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=75)
    seat_no = models.IntegerField()
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
    user_id = models.ForeignKey(RegisteredUser, on_delete=models.SET_NULL, null=True, blank=True, default = None)

    def __str__(self):
        if self.user_id is not None:
            return str(self.user_id.name) + "'s ticket for screening " + str(self.screening_id) + " seat number " + str(self.seat_no)
        else:
            return "Anonymous ticket for " + str(self.screening_id) + " seat number " + str(self.seat_no)

class Payment(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    user_id = models.ForeignKey(RegisteredUser, on_delete=models.SET_NULL, null=True, blank=True, default = None)

    def __str__(self):
        if self.user_id is not None:
            return "Payment #" + str(self.id) + " by " + str(self.user_id)
        else:
            return "Payment #" + str(self.id) + " by an anonymous user"

class PaymentForTicket(models.Model):
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)

class SavedDebit(models.Model):
    user_id = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    debit_number = models.CharField(max_length=20)

class SavedCredit(models.Model):
    user_id = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    credit_number = models.CharField(max_length=20)