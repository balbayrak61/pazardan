from django.urls import path
from .views import product_list, product_list_by_category, product_detail, product_delate
from .views import cart_detail, cart_add, cart_remove, cart_update, checkout
from .views import register, login_view, logout_view, orders_list, add_product, add_category
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', product_list, name='product_list'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('category/<int:category_id>/', product_list_by_category, name='product_list_by_category'),
    path('product/detail/<int:id>/', product_detail, name='product_detail'),
    path('product/delate/<int:id>/', product_delate, name='product_delate'),
    path('cart/', cart_detail, name='cart_detail'),
    path('add-product/', add_product, name='add_product'),
    path('add-category/', add_category, name='add_category'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart/update/', cart_update, name='cart_update'),
    path('checkout/', checkout, name='checkout'),
    path('products/', product_list, name='product_list'),
    path('orders/', orders_list, name='orders_list'),
]

# Static and media file serving (only during development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
