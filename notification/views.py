from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Login, SendEmail
from notification.serializers import LoginSerializer, SendEmailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .commons.responses import *
#from .serializers import LoginSerializer, SendEmailSerializer



class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'auth': True,
                    'token': str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Se requieren nombre de usuario y contraseña'}, status=status.HTTP_400_BAD_REQUEST)


class SendEmailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            # Lógica para enviar el correo
            uuid = serializer.validated_data['uuid']
            body = serializer.validated_data['body']
            email = serializer.validated_data['email']
            title = serializer.validated_data['title']
            
            # Aquí agregarías la lógica para enviar el correo
            # Por ejemplo, usando send_mail() de Django o algún otro servicio

            return Response({
                'date': 'fecha_envio_del_correo',  # Aquí puedes usar la fecha real
                'message': 'mensaje_de_envio_correcto'
            }, status=status.HTTP_200_OK)
        # return Response({'error': 'Datos no proporcionados correctamente'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(bad_request_response, status=status.HTTP_400_BAD_REQUEST)


# class NotificationAPIView(APIView):
#     def get(self, request):
#         serializer = NotificationSerializer(Notification.objects.all(),many=True)
    
#         return Response(status=status.HTTP_200_OK, data=serializer.data)


#     def post(self, request):
#         x = request.data
#         print(f"HERE-> {x}")
#         data = Notification.objects.create(uuid=request.data['uuid'],body=request.data['body'], email=request.data['email'],title=request.data['title'])

        
#         return self.get(data)
