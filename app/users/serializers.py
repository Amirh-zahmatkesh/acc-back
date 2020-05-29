from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    # TODO
    # certificates = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Ingredient.objects.all()
    # )
    # videos = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all()
    # )

    class Meta:
        model = get_user_model()
        # TODO add certificates and videos
        fields = ('id', 'email', 'password', 'first_name', 'last_name',
                  'phone_number', 'credit', 'points')
        extra_kwargs = {'password': {'write_only': True,
                                     'label': 'گذرواژه', 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField(label='ایمیل')
    password = serializers.CharField(
        style={'input_type': 'password'}, label='گذرواژه',
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class UserImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to users"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'image')
        read_only_fields = ('id',)
