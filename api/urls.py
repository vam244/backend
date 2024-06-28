from django.contrib import admin
from django.urls import path,include
from knox import views as knox_views
from . import views
urlpatterns = [
    #home
    path('', views.getRoutes,name="routes"),
    #main page
    path('current_user/',views.get_user_by_token,name="user"),
    path('products/', views.getproducts,name="products"),
    path('products/<str:x>',views.getproduct,name="product"),
    path('products/<str:x>/update',views.update_product,name="update_product"),
    #cart
    path('cart/', views.getcart_products,name="cart_products"),
    path('cart/<str:x>/update',views.update_cart_product,name="update_cart_product"),
    path('cart/create',views.addtocart,name="addtocart"),
    path('cart/<str:x>/delete',views.deleteitem,name="deleteitem"),
    #authentication
    path('register/',views.register_api,name='reg'),
    path('login/',views.login_api,name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
