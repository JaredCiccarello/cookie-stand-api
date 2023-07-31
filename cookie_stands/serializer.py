from rest_framework import serializers
from .models import CookieStand

class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'location', 'owner', 'description', 'hourly_sales', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale')
        model = CookieStand


# from rest_framework import serializers
# from .models import CookieStand


# class cookie_standserializer(serializers.ModelSerializer):
#     class Meta:
#         model = CookieStand
#         fields = "__all__"
