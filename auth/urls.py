from django.urls import path
from auth.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^$', schema_view),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterView.as_view(), name='auth_register'),
]