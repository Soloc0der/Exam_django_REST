
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as drf_get_schame_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schame_view = drf_get_schame_view(
    openapi.Info(
        title="Django-rest",
        description="APi description",
        default_version="v1",
        terms_of_service="https://t.me/solo_coder/",
        contact=openapi.Contact(email="Khurshidoff2707@gmail.com")
    ),
    public=True,
    permission_classes=(AllowAny, )

) 





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("api.urls")),
    path("schame/", get_schema_view(title="Exam APi", description="Shunchaki test sifatida yozilgan APi", version="1.0.5") , name="openapi-schame"),
    path("swagger/", schame_view.with_ui("swagger", cache_timeout=0), name="swagger-docs"),
    path("redoc/", schame_view.with_ui("redoc", cache_timeout=0), name="redoc-docs"),
    path('', include('main.urls'))
    
]
