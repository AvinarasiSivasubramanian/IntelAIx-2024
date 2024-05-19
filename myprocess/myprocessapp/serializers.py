from rest_framework import serializers
from .models import ProcessParameterSample, ProcessParameter

class ProcessParameterSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessParameterSample
        fields = '__all__'

class ProcessParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessParameter
        fields = '__all__'
