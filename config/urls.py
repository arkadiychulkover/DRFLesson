from django.urls import path, include

urlpatterns = [
    # path('api/', include('DRF_EXAMPLE.urls')),
    path('api/', include('MoviePlanetApi.urls')),
]
