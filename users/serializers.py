from rest_framework.serializers import ModelSerializer

from education.serializers import PaymentSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class UserLimitedSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_name')
