from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer


class UserList(generics.ListAPIView):
    """ Вывод списка пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="Список пользователей")
    def get(self, request, *args, **kwargs):
        return super(UserList, self).get(request, *args, **kwargs)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    @swagger_auto_schema(operation_summary="Создание пользователя")
    def post(self, request, *args, **kwargs):

        return super(UserCreateView, self).post(request, *args, **kwargs)

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(self.request.data["password"])
        new_user.save()


class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()

    @swagger_auto_schema(operation_summary="Изменение пользователя")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Изменение пользователя")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()

    @swagger_auto_schema(operation_summary="Удаление пользователя")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)