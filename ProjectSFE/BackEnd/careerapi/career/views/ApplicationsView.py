from django.shortcuts import render
from ..serializers import OfferApplicationSerializer

from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import django.db
from ..models  import OfferApplication,Intern,InternShipOffer
#DOWNLOAD
import os
from django.conf import settings
from django.http import HttpResponse, Http404


@api_view(['POST'])
def CreateApplication(request):
    try:
        application=OfferApplication()
        application.intern=Intern.objects.get(id=request.data.get('intern'))
        application.internShipOffer=InternShipOffer.objects.get(id=request.data.get('internShipOffer'))
        application.ApplicationText=request.data.get('ApplicationText')
        cv = request.FILES['cv']
        print(request.data)
        application.cv=cv
        application.save()
        return Response('Saved')
    except:
        return Response('Not Saved')
    
    
@api_view(['POST'])
def UpdateApplication(request):
    id=request.data['id']
    offerApplication=OfferApplication.objects,get(id=id)
    serializer=OfferApplicationSerializer(instance=offerApplication,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Updated')
    else:
        return Response('Not Updated')
@api_view(['GET'])
def ApplicationById(request):
    id=request.GET.get('id')
    offerApplication=OfferApplication.objects.get(id=id)
    serializer=OfferApplicationSerializer(offerApplication,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ApplicationsByInternShipOffer(request):
    internShipOffer=request.GET.get('internShipOffer')
    offerApplications=OfferApplication.objects.filter(internShipOffer=internShipOffer)
    serializer=OfferApplicationSerializer(offerApplications,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def ApplicationsByIntern(request):
    intern=request.GET.get('intern')
    offerApplications=OfferApplication.objects.filter(intern=intern)
    serializer=OfferApplicationSerializer(offerApplications,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def DownloadCv(request):
    path=request.GET.get('filePath')
    print(path[7:])
    path=path[7:]
    file_path =os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
