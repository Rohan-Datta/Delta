from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ItemsAPI.models import Laptop, Server, Accessory, GPU
from ItemsAPI.serializers import LaptopSerializer, ServerSerializer, AccessorySerializer, GPUSerializer
from django.http import Http404

# Lists all laptops
class LaptopList(APIView):
    def get(self, request):
    	laptops = Laptop.objects.all()

    	serializer = LaptopSerializer(laptops, many=True)
    	return Response(serializer.data)

# Get individual laptop details
class LaptopDetail(APIView):

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = LaptopSerializer(snippet)
        return Response(serializer.data)


# Lists all servers
class ServerList(APIView):
    def get(self, request):
    	servers = Server.objects.all()

    	serializer = ServerSerializer(servers, many=True)
    	return Response(serializer.data)

# Get individual server details
class ServerDetail(APIView):

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ServerSerializer(snippet)
        return Response(serializer.data)

# Lists all accessory
class AccessoryList(APIView):
    def get(self, request):
    	accessories = Accessory.objects.all()

    	serializer = LaptopSerializer(accessories, many=True)
    	return Response(serializer.data)

# Get individual accessory details
class AccessoryDetail(APIView):

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = AccessorySerializer(snippet)
        return Response(serializer.data)

# Lists all GPUs
class GPUList(APIView):
    def get(self, request):
    	gpu = GPU.objects.all()

    	serializer = GPUSerializer(gpu, many=True)
    	return Response(serializer.data)

# Get individual GPU details
class GPUDetail(APIView):

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = GPUSerializer(snippet)
        return Response(serializer.data)