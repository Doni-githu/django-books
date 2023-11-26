from . import models, serializers, tasks
from rest_framework.views import APIView
from rest_framework.response import Response
class Registeration(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        created = models.User(name, email)
        data = {
            'createdAt': created.createdAt,
            'name': created.name,
            'email': created.email
        }
        tasks.send_welcome_email.delay(email)
        return Response({"message": 'We are sent to your email account a welcome letter'})