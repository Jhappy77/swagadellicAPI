from swagDB.views import registerUser
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index',),
    path('movie', views.movie.as_view(), name='movie'),
    path('screening', views.screening, name='screening'),
    path('movies', views.movies.as_view(), name='movies'),
    path('early-movies', views.moviesWithEarlies.as_view(), name='early-movies'),
    path('register-user', views.registerUser.as_view(), name='register-user'),
    path('save-credit', views.saveCredit.as_view(), name='save-credit'),
    path('save-debit', views.saveDebit.as_view(), name='save-debit'),
    path('save-ticket', views.saveTicket.as_view(), name='save-ticket'),
    path('save-payment', views.savePayment.as_view(), name='save-payment'),
    path('login', views.login.as_view(), name='login'),
]