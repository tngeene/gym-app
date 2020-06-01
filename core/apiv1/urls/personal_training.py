from django.urls import path

from ..views.personal_training import (BookingCreateAPIView,AcceptPersonalTrainingAPIView,
                                       BookingHistoryListAPIView)

app_name = 'personal_training'

urlpatterns = [
    path('create/',BookingCreateAPIView.as_view(),name='book_trainer'),
    path('all/',BookingHistoryListAPIView.as_view(),name='my_personal_training_sessions'),
    path('accept/',AcceptPersonalTrainingAPIView.as_view(),name='accept_personal_training_request'),
]
