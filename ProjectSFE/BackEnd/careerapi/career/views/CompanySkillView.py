from django.shortcuts import render
from ..serializers import CompanySkillSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import CompanySkill

@api_view(['GET'])
def CompanySkills(request):
    CompanyId=request.GET.get('CompanyId')
    companySkills=CompanySkill.objects.filter(company=CompanyId)
    serializer=CompanySkillSerializer(companySkills,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def CreateCompanySkill(request):
    serializer=CompanySkillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Saved')
    else:
        return Response('Not Saved')

@api_view(['POST'])
def UpdateCompanySkill(request):
    id=request.data['id']
    companySkill=CompanySkill.objects.get(id=id)
    serializer=CompanySkillSerializer(instance=companySkill,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Updated')
    else:
        return Response('Not Updated')
@api_view(['DELETE'])
def DeleteCompanySkill(request):
    id=request.GET.get('id')
    companySkill=CompanySkill.objects.get(id=id)
    companySkill.delete()
    return Response('Deleted')
