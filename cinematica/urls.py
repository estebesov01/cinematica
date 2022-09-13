from django.contrib import admin
from rest_framework_simplejwt.views import \
    TokenObtainPairView, TokenRefreshView, TokenVerifyView

from patches import routers
from django.urls import path, include, re_path
from movies.urls import router1
from payment.urls import router2
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.extend(router1)
router.extend(router2)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('djoser.urls'), name='user'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('jwt/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('jwt/token/verify',
         TokenVerifyView.as_view(),
         name='token_verify'),
]
urlpatterns += doc_urls
