from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.index_view ),
    path('hydjobs',views.hydjobs_view),
    path('banglorejobs',views.banglorejobs_view),
    path('punejobs',views.punejobs_view)
]
