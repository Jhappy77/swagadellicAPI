from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "movie_name", "genre", "release_date", "length")

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ("id", "theatre_name", "address", "theatre_type")

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("seat_no",)

class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = ("id", "screening_time") #"movie_id", "theatre_id", 

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("ticket_id", "seat_no", "screening_id", "user_id")

class SavedDebitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedDebit
        fields = ("id", "user_id", "debit_number")

class SavedCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedCredit
        fields = ("id", "user_id", "credit_number")

class RegisteredUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ("name", "birthdate", "password", "email")

class RegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ("name", "birthdate", "email")

class SavedDebitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedDebit
        fields = ("user_id", "debit_number")

class SavedCreditCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedCredit
        fields = ("user_id", "credit_number")

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("amount", "user_id")
