from rest_framework import serializers
from .models import Dsc, STATUS_CHOICES

class DscSerializers(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	class Meta:
		model = Dsc
		fields = (
		'id',
		'author',
		'status',
		'lead',
		'name',
		'gmail',
		'city',
		'state',
		'team_size',
		'established_on',
		'created_on',
		'updated_on',
		'cover',
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