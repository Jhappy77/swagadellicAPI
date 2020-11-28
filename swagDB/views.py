from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import status


from .models import *
from .serializers import *

from datetime import datetime, timedelta

def index(request):
    return HttpResponse("Pong! You hit the swagDB index.")
# Create your views here.


class movie(APIView):
    #permission_classes=(IsAuthenticated,)
    def get(self, request):

        # if(request.method == 'GET'):
        #     #dosomething
        # elif(request.method == 'POST'):

        msg = request.query_params.get('movieName', "World")
        reply = 'Hello ' + msg + ' !'
        content = {'message': reply}
        return Response(content)


#TODO: Should hash and salt passwords. But that's beyond the scope of this project, really
class login(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        myusername = request.query_params.get('email', None)
        queryset = RegisteredUser.objects.all().filter(email=myusername)
        if not queryset.exists():
            return Response({'Login error': 'No username with that email found!'}, status=status.HTTP_400_BAD_REQUEST)
        mypassword = request.query_params.get('password', None)
        queryset = queryset.filter(password=mypassword)
        if not queryset.exists():
            return Response({'Login error': 'You entered the wrong password!'}, status=status.HTTP_400_BAD_REQUEST)
        res = RegisteredUserSerializer(queryset[0])
        return Response(res.data)

class theatreScreening(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        theatreId = request.query_params.get('theatreId', None)
        movieId = request.query_params.get('movieId', None)
        if ((theatreId is None) or (movieId is None)):
            return Response({'Error': 'Query must include theatreId and movieId'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = Theatre.objects.all().filter(theatre_id=theatreId).filter(movie_id=movieId)
        res = ScreeningSerializer(queryset)
        return Response(res.data)

class theatreWithMovie(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        movieId = request.query_params.get('movieId', None)
        if ((movieId is None)):
            return Response({'Error': 'Query must include movieId'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = Screening.objects.filter(movie_id=movieId).select_related('theatre_id')
        res = TheatreSerializer(queryset)
        return Response(res.data)

class movies(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class moviesWithEarlies(generics.ListAPIView):
    two_weeks_future = datetime.now() + timedelta(days=14)
    queryset = Movie.objects.all().filter(release_date__range=["2011-01-01", two_weeks_future])
    serializer_class = MovieSerializer

#TODO: Should hash and salt passwords. But that's beyond the scope of this project, really
class registerUser(generics.CreateAPIView):
    queryset = RegisteredUser.objects.all()
    serializer_class = RegisteredUserCreateSerializer

class saveCredit(generics.CreateAPIView):
    queryset = SavedCredit.objects.all()
    serializer_class = SavedCreditCreateSerializer

class saveDebit(generics.CreateAPIView):
    queryset = SavedDebit.objects.all()
    serializer_class = SavedDebitCreateSerializer

class saveTicket(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class savePayment(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = PaymentCreateSerializer




# def movie (request):
#     movieName = request.content_params.get('movieName', 'Shrek 2')

#     return HttpResponse("Movie name was: " + movieName)

def screening (request):
    screeningName = request.content_params.get('screeningName', 'Jeff')
    return HttpResponse(screeningName)