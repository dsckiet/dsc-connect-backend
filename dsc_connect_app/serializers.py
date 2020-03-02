from rest_framework import serializers
from .models import Dsc, STATUS_CHOICES, User

class DscSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	class Meta:
		model = Dsc
		fields = (
		'id',
		'author',
		'status',
		'lead',
		'name',
		'quote',
		'domains',
		'gmail',
		'city',
		'state',
		'country',
		'team_size',
		'established_on',
		'created_on',
		'updated_on',
		'website',
		'github',
		'medium',
		'facebook',
		'twitter',
		'linkedin',
		'instagram',
		'youtube',
		'behance',
		'custom',
				)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'gender',
            'is_admin',
            'is_worker',
            'is_volunteer',
            'date_joined',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['pk']

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Email should be unique")
        return value

    # TODO: Finalize phone number structure
    def validate_phone_number(self, value):
        if value[0] == '+':
            value = value[1:]
        if 8 <= len(value) <= 10:
            return value

    # TODO: Validate password based on numbers, special characters, uniqueness
    def validate_password(self, value: str) -> str:
        if len(value) < 7:
            raise serializers.ValidationError("Password Length should be greater than 8")
        else:
            return make_password(value)