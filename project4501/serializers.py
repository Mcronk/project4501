from rest_framework import serializers

from project4501.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #ommiting courses temporarily
        fields = ('user_id', 'name', 'password', 'email', 'phone', 'description', 'grade')
