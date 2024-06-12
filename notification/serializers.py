from rest_framework.serializers import ModelSerializer
from notification.models import Login, SendEmail

class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        #fields = '__all__' # Esto no es recomendable
        fields = ['username','password']


class SendEmailSerializer(ModelSerializer):
    class Meta:
        model = SendEmail
        #fields = '__all__' # Esto no es recomendable
        fields = ['uuid','body','email','title','created','modified']