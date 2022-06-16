from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .TransactionsModels import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['payment_method','credit_card_number','amount','barcode','payment_date']

class TotalTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['payment_date','amount']