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
            'username',
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


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)