from rest_framework import serializers 

class ProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()