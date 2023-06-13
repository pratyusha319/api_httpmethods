from django.shortcuts import render
from app.models import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from app.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

# @api_view()
# @permission_classes(IsAuthenticated)
# def produt_c_d(request):
#     PQS=Product_category.objects.all()
#     PQD=Product_c_s(PQS,many=True)
#     return Response(PQD.data)

class productjd(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PQD=Product_s(PQS,many=True)
        return Response(PQD.data)
    

    def post(self,request,id):
        pmsd=Product_s(data=request.data)
        if pmsd.is_valid():
            spo=pmsd.save()
            return Response({'message':'product is created'})
       
        return Response({'message':'product creation is failed'})

    def put(self,request,id):
        id=request.data['id']
        po=Product.objects.get(id=id)
        upo=Product_s(po,data=request.data)
      
        if upo.is_valid():
            spo=upo.save()
            return Response({'message':'product is updated'})
       
        return Response({'message':'product updation is failed'})

    def patch(self, request, id):
        id=request.data['id']
        po=Product.objects.get(id=id)
        upo=Product_s(po,data=request.data,partial=True)
      
        if upo.is_valid():
            spo=upo.save()
            return Response({'message':'product is updated'})
       
        return Response({'message':'product updation is failed'})

        

    def delete(self, request, id ):
        
        product = Product.objects.get(id=id)
        product.delete()
        return Response({'success': 'Product is deleted'})

# @api_view()
# @permission_classes(IsAuthenticated)
# def produtjd(request):
#     PQS=Product.objects.all()
#     PQD=Product_s(PQS,many=True)
#     return Response(PQD.data)