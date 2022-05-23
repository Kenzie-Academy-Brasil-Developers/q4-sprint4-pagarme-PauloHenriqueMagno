from rest_framework.urls import path

from products.views import ProductView, ProductGetPatchView, ProductsBySellerId

urlpatterns = [
  path('products/', ProductView.as_view()),
  path('products/<str:product_id>/', ProductGetPatchView.as_view()),
  path('products/seller/<str:seller_id>/', ProductsBySellerId.as_view()),
]