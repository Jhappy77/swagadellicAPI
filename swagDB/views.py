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

class screeningByTheatreMovie(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        theatreId = request.query_params.get('theatreId', None)
        movieId = request.query_params.get('movieId', None)
        if ((theatreId is None) or (movieId is None)):
            return Response({'Error': 'Query must include theatreId and movieId'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = Screening.objects.all().filter(theatre_id=theatreId).filter(movie_id=movieId)
        reslist = []
        for query in queryset:
            reslist.append(ScreeningSerializer(query).data)
        return Response(reslist)

class theatreWithMovie(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        movieId = request.query_params.get('movieId', None)
        if ((movieId is None)):
            return Response({'Error': 'Query must include movieId'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = Screening.objects.filter(movie_id=movieId).select_related('theatre_id')
        reslist = []
        for screening in queryset:
            reslist.append(TheatreSerializer(screening.theatre_id).data)
        return Response(reslist)

class bookedSeats(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        screeningId = request.query_params.get('screeningId', None)
        if ((screeningId is None)):
            return Response({'Error': 'Query must include screeningId'}, status=status.HTTP_400_BAD_REQUEST)
        tickets = Ticket.objects.filter(screening_id=screeningId)
        reslist = []
        for ticket in tickets:
            reslist.append(SeatSerializer(ticket).data)
        seatlist = []
        for res in reslist:
            seatlist.append(res.get("seat_no"))
        return Response(seatlist)

class lookForTicket(APIView):
    def get(self, request):
        if(request.method != 'GET'):
            return Response({'Error': 'Method not GET'}, status=status.HTTP_400_BAD_REQUEST)
        ticketId = request.query_params.get('ticketId', None)
        if ((ticketId is None)):
            return Response({'Error': 'Query must include ticketId'}, status=status.HTTP_400_BAD_REQUEST)
        tickets = Ticket.objects.filter(ticket_id=ticketId)
        if not tickets.exists():
            return Response ({'Error': 'No ticket with requested id exists'}, status=status.HTTP_204_NO_CONTENT)
        return Response(TicketSerializer(tickets[0]).data)

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

# def screening (request):
#     screeningName = request.content_params.get('screeningName', 'Jeff')
#     return HttpResponse(screeningName)