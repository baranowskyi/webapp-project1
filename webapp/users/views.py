from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from users import serializers
from users.models import UserSite


@extend_schema_view(
    post=extend_schema(summary='Registration', tags=['Reg And Login']),
)
class RegistrationView(CreateAPIView):
    queryset = UserSite.objects.all()
    serializer_class = serializers.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(
        request=serializers.ChangePasswordSerializer, 
        summary='Change Password', tags=['Reg And Login']),
)
class ChangePasswordView(APIView):
    def post(self, request):
        user = request.user
        serializer = serializers.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)


@extend_schema_view(
    get=extend_schema(summary='Profile', tags=['Users']),
    put=extend_schema(summary='Edit Profile', tags=['Users']),
    patch=extend_schema(summary='Edit Small', tags=['Users']),
)
class MeView(RetrieveUpdateAPIView):
    queryset = UserSite.objects.all()
    serializer_class = serializers.MeSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return serializers.MeUpdateSerializer
        return serializers.MeSerializer
    
    def get_object(self):
        return self.request.user
