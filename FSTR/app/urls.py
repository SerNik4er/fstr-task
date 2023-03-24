from django.urls import path
from .views import *

urlpatterns = [
    path('submitData', PerevalAddAPI.as_view()),
    path('submitData/<int:pk>/', PerevalDetailAPI.as_view({'get': 'retrieve', 'path': 'partial_update'})),
    path('submitData/user__email=<str:email>', AuthEmailPerevalAPI.as_view({'get': 'list'}))
]