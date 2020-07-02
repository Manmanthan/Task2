from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from bank_branches.models import Banks, Branches
from bank_branches.serializers import BankSerializer, BranchSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Banks.objects.all().order_by('id')
    serializer_class = BankSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
