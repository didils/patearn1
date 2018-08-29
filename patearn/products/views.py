from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers, jsons
from rest_framework import status
from rest_framework.response import Response

class UploadProducts(APIView):

    def get(self, request, format=None):

        jsons_data = jsons.jsons


        for json in jsons_data:
            models.Product.objects.create(**json)

        return Response(status=status.HTTP_200_OK)

        """
        serializer = serializers.ProductSerializer(data=request.data)
        print(serializer)
        
        if serializer.is_valid():
            
            print(serializer.data)
            
            models.Product.objects.create(**json)
            print(models.Product.objects.all())

            return Response(status=status.HTTP_200_OK)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """
        
