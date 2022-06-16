from django.contrib import admin
from .models import Boleta
from .TransactionsModels import Transaction

admin.site.register(Boleta)
admin.site.register(Transaction)