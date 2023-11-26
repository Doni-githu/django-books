from . import models, serializers, tasks
from rest_framework.views import APIView
from rest_framework.response import Response

class Registeration(APIView):
    def post(self, request):
        name = request.data["name"]
        email = request.data["email"]
        result = tasks.send_welcome_email(email)
        return Response(
            {"message": "We are sent to your email account a welcome letter"}
        )
