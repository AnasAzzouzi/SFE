from django.shortcuts import render
from ..serializers import LocationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Location

@api_view(['GET'])
def AllLocations(request):
    locations=Location.objects.all()
    serializer=LocationSerializer(locations,many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def LocationById(request):
    idLocation=request.GET.get('id')
    location=Location.objects.get(id=idLocation)
    serializer=LocationSerializer(location,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def CreateLocation(request):
    serializer=LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Created')
    else:
        return Response("Sorry SomeThing Went Wrong !")

@api_view(['POST'])
def UpdateLocation(request):
    idLocation=request.data['id']
    location=Location.objects.get(id=idLocation)
    serializer =LocationSerializer(instance=location,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Updated')
    else:
        return Response("Sorry SomeThing Went Wrong !")
@api_view(['DELETE'])
def DeleteLocation(request):
    idLocation=request.GET.get('id')
    location=Location.objects.get(id=idLocation)
    location.delete()
    return Response('Deleted')
