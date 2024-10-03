from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView, TokenVerifyView
from rest_framework import routers, permissions

from cats.views import KittyViewSet, BreedViewSet, RatingViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Kitten API",
        default_version='v1',
        description="Kitty app endpoints descriptions",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

router = routers.SimpleRouter()
router.register(r'kitten', KittyViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('swagger<format>/',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('api/v1/', include(router.urls))
]
