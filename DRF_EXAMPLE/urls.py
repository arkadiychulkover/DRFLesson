from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product/<uuid:id>/', views.ProductAPIView.as_view(), name='product-detail'),
    path('sample/', views.ExampleAPIView.as_view(), name='sample-api'),
    
    path('projects/', views.ProjectAPIView.as_view(), name='project-list'),
    path('projects/<uuid:id>/', views.ProjectAPIView.as_view(), name='project-detail'),
    
    path('tasks/', views.TaskAPIView.as_view(), name='task-list'),
    path('tasks/<uuid:id>/', views.TaskAPIView.as_view(), name='task-detail'),
]