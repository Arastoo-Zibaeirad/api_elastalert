from django import http
from django.http import response
from django.shortcuts import render
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Rule
from .serializers import RuleSerializer

# Create your views here.

@api_view(["GET"])
def rule_list(request):
    rule = Rule.objects.all()
    rule_serialize = RuleSerializer(rule, many=True)
    return Response(rule_serialize.data)

@api_view(["GET"])
def rule_detail(request, pk):
    try:
        rule = Rule.objects.get(id=pk)
    except:
        return response.HttpResponse(status=404)
    rule_serialize = RuleSerializer(rule, many=False)
    return Response(rule_serialize.data)
    
@api_view(["POST"])
def rule_save(request):
    rule = RuleSerializer(data=request.data)
    
    if rule.is_valid():
        rule.save()
        return Response(rule.data, status=201)
    return Response()

@api_view(["POST"])
def rule_update(request, pk):
    instance = Rule.objects.get(id=pk)
    rule = RuleSerializer(instance=instance, data=request.data)
    if rule.is_valid():
        rule.save()
    
    return Response()

@api_view(["DELETE"])
def rule_delete(request, pk):
    instance = Rule.objects.get(id=pk)
    # rule = RuleSerializer(instance=instance, data=request.data)
    # if rule.is_valid():
    #     rule.save()
    instance.delete()
    return Response("Rule Deleted")
