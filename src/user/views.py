from book import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class Registeration(APIView):
    def post(self, request):
        print(request.data)
        return Response({"message": "Doniyor Doniyorov"})