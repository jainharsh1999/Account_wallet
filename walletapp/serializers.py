from rest_framework import serializers
from .models import wallet

class walletSerializer(serializers.ModelSerializer):
	class Meta:
		model = wallet 
		fields ='__all__'	