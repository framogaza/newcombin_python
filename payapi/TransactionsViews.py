from django.http import JsonResponse

from payapi.TransactionsSerializers import TransactionSerializer
from .TransactionsModels import Transaction
from .TransactionsSerializers import TransactionSerializer
from .TransactionsSerializers import TotalTransactionsSerializer
from .serializers import BoletaSerializer
from .serializers import BoletasImpagasFiltroSerializer
from .serializers import BoletasImpagasSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from payapi import serializers


@api_view(['POST'])
def new_transaction(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)


@api_view(['GET'])
def list_transaction(self):
    dateFrom =  self.query_params.get('dateFrom')
    dateTo = self.query_params.get('dateTo')
    transaction = Transaction.objects.filter(payment_date__gte=dateFrom,payment_date__lte=dateTo)
    serializer = TotalTransactionsSerializer(transaction,many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def list_transaction2(request):

    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions,many=True)
        return JsonResponse({"transactions": serializer.data},safe = False)

