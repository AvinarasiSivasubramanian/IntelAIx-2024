#from django.shortcuts import render
'''from rest_framework import generics
from .models import ProcessParameterSample, ProcessParameter
from .serializers import ProcessParameterSampleSerializer, ProcessParameterSerializer

class ProcessParameterSampleCreateAPIView(generics.CreateAPIView):
    queryset = ProcessParameterSample.objects.all()
    serializer_class = ProcessParameterSampleSerializer

class ProcessParameterCreateAPIView(generics.CreateAPIView):
    queryset = ProcessParameter.objects.all()
    serializer_class = ProcessParameterSerializer
'''

'''from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProcessParameterSample, ProcessParameter
from .serializers import ProcessParameterSampleSerializer, ProcessParameterSerializer

@api_view(['GET'])
def process_parameter_sample_list(request):
    samples = ProcessParameterSample.objects.all()
    serializer = ProcessParameterSampleSerializer(samples, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def process_parameter_sample_create(request):
    serializer = ProcessParameterSampleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def process_parameter_list(request):
    parameters = ProcessParameter.objects.all()
    serializer = ProcessParameterSerializer(parameters, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def process_parameter_create(request):
    serializer = ProcessParameterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
'''

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ProcessParameterSample, ProcessParameter
from .serializers import ProcessParameterSampleSerializer, ProcessParameterSerializer

@api_view(['GET', 'POST'])
def process_parameter_sample_list(request):
    if request.method == 'GET':
        samples = ProcessParameterSample.objects.all()
        serializer = ProcessParameterSampleSerializer(samples, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProcessParameterSampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def process_parameter_list(request):
    if request.method == 'GET':
        parameters = ProcessParameter.objects.all()
        serializer = ProcessParameterSerializer(parameters, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProcessParameterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

