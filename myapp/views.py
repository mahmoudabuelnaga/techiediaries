from django.shortcuts import render
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Family, Location, Transaction
from .serializers import ProductSerializer, FamilySerializer, LocationSerializer, TransactionSerializer

class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FamilyListAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FamilyDetailApi(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LocationListAPI(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocatinDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TransectionListAPI(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransectionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# @api_view(['GET','POST'])
# def products_list_api(request):
#     """
#         List Produsts or create a new Product.
#     """
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, context={'request':request}, many=True)
#         return Response(serializer.data)    
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def product_detail_api(request, pk):
#     """
#         retrieve, update and delete product instance.
#     """
#     try:
#         product = Product.objects.get(pk=pk)
    
#     except Product.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = ProductSerializer(product, context={'request':request})
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET','POST'])
# def familys_list_api(request):

#     """
#         List Familys and create a new family.
#     """

#     if request.method == 'GET':
#         familys = Family.objects.all()
#         serializer = FamilySerializer(familys, context={'request':request}, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = FamilySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    
# @api_view(['GET','PUT','DELETE'])
# def family_detail_api(request, pk):

#     """
#         retrive, update and destroy family instance.
#     """

#     try:
#         family = Family.objects.get(pk=pk)
    
#     except Family.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = FamilySerializer(family, context={'request':request})
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = FamilySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         family.delete()
#         return Response(status=status.HTTP_204_No_CONTENT)




# @api_view(['GET','POST'])
# def locations_list_api(request):
#     """
#         list locations and create a new location.
#     """
#     if request.method == 'GET':
#         locations = Location.objects.all()
#         serializer = LocationSerializer(locations, context={'request':request}, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# @api_view(['GET','PUT','DELETE'])
# def location_detail_api(request, pk):
#     """
#         retrive , update and destroy loctaion instance.
#     """
#     try:
#         location = Location.objects.get(pk=pk)
    
#     except Location.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = LocationSerializer(location, context={'request':request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET','POST'])
# def transactions_list_api(request):
#     """
#         List transactions and create a new transection.
#     """
#     if request.method == 'GET':
#         transactions = Transaction.objects.all()
#         serializer = TransactionSerializer(transactions, context={'request':request}, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TransactionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','PUT','DELETE'])
# def transaction_detail_api(request, pk):

#     """
#         retrive, update and delete transection instance.
#     """

#     try:
#         transaction = Transaction.objects.get(pk=pk)

#     except Transaction.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = TransactionSerializer(transaction, context={'request':request})
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = TransactionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         transaction.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)