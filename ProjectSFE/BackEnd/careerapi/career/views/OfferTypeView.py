from django.shortcuts import render
from ..serializers import OfferTypeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import OfferType


@api_view(['GET'])
def AllOfferTypes(request):
    offerTypes=OfferType.objects.all()
    serializer=OfferTypeSerializer(offerTypes,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def CreateOfferType(request):
    serializer=OfferTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Added")
    else:
        print(serializer.errors)
        return Response("Sorry SomeThing When Wrong Please Retry")

@api_view(['POST'])
def UpdateOfferType(request):
    id=request.data['id']
    offerType=OfferType.objects.get(id=id)
    serializer=OfferTypeSerializer(instance=offerType,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Updated")
    else:
        return Response("Sorry SomeThing When Wrong Please Retry")
@api_view(['DELETE'])
def DeleteOfferType(request):
    id=request.GET.get('id')
    offerType=OfferType.objects.get(id=id)
    offerType.delete()
    return Response('Deleted')
