from django.http import JsonResponse
from .models import Boleta
from .serializers import BoletaSerializer
from .serializers import BoletasImpagasFiltroSerializer
from .serializers import BoletasImpagasSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from payapi import serializers

@api_view(['POST'])
def boleta_nueva(request):
    if request.method == 'POST':
        serializer = BoletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)

@api_view(['GET'])
def boleta_listado(request):

    if request.method == 'GET':
        boletas = Boleta.objects.all()
        serializer = BoletaSerializer(boletas,many=True)
        return JsonResponse({"boletas": serializer.data},safe = False)

@api_view(['GET'])
def boletas_impagas_filtro(request,tipoServicio):

    boletas = Boleta.objects.filter(tipo=tipoServicio,estado='pending').values()
    if request.method == 'GET':
        serializer = BoletasImpagasFiltroSerializer(boletas,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def boletas_impagas(request):

    boletas = Boleta.objects.filter(estado='pending').values()
    if request.method == 'GET':
        serializer = BoletasImpagasSerializer(boletas,many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def boleta_detalle(request,codigoBarra):

    try:
        boleta = Boleta.objects.get(pk=codigoBarra)
    except Boleta.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoletaSerializer(boleta)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BoletaSerializer(boleta,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        boleta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
