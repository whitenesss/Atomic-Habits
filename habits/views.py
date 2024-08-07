from django.shortcuts import render
from rest_framework import generics, viewsets

from habits.models import Habit
from habits.serializer import HabitSerializer, HabitCreateSerializer


# Create your views here.
class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


# class HabitConnectionSet(viewsets.ModelViewSet):
#     queryset = HabitConnection.objects.all()
#     serializer_class = HabitConnectionSerializer
