from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

# User = get_user_model()



class RegistrationSerializer(RegisterSerializer):
    class Meta:
        model = CustomUser
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    personal_id = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.userprofile.personal_id = self.validated_data.get(
            'personal_id', '')

        user.save(update_fields=['first_name', 'last_name'])
        user.userprofile.save(update_fields=['org_id'])