from rest_framework import serializers

from bank_branches.models import Branches, Banks


class BankSerializer(serializers.ModelSerializer):
    branches = serializers.SerializerMethodField()

    def get_branches(self, request):
        bank_branches = Branches.objects.filter(bank_id=request)
        return BranchSerializer(bank_branches, many=True).data

    class Meta:
        model = Banks
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'