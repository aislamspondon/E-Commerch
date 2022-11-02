from base.views import product_views as views
from django.urls import path

urlpatterns = [
    path('top/', views.getTopProducts, name='top-products'),
    path('', views.getProducts, name='products'),
    path('create/', views.createProduct, name='create-product'),
    path('upload/', views.uploadImage, name='image-upload'),
    path('<str:pk>/reviews/', views.createProductReview, name='product-review'),
    path('<str:pk>', views.getProduct, name='product'),
    path('delete/<str:pk>', views.deleteProduct, name='product-delete'),
    path('update/<str:pk>', views.updateProduct, name='product-update'),
]
