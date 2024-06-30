from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.apps import UsersConfig
from users.views import UserList, UserCreateView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]