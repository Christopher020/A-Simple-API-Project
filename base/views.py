from django.shortcuts import render
from django.http import HttpResponse
from .models import Slack
from .serializers import SlackSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def home(request):
    get_slack_objects = Slack.objects.all()
    serializer = SlackSerializer(get_slack_objects, many=True)
    return Response(serializer.data)