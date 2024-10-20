from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Event, Category
from .serializers import EventSerializer


class EventListCreateView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpcomingEventListView(APIView):
    def get(self, request):
        today = timezone.now().date()
        tomorrow = today + timezone.timedelta(hours=24)
        events = Event.objects.filter(date__range=[today, tomorrow])
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventListByCategoryView(APIView):
    def get(self, request, category_name):
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        events = Event.objects.filter(category=category)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
