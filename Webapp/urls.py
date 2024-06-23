from django.urls import path
from Webapp import views
urlpatterns=[
    path('',views.homepage,name="home"),
    path('About/',views.aboutpage,name="About"),
    path('Contact/',views.Contactpage,name="Contact"),
    path('Product/',views.Productpage,name="Product"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
    path('single_page/<int:pro_id>/',views.single_page,name="single_page"),
    path('register_page/',views.register_page,name="register_page"),

path('save_register/',views.save_register,name="save_register"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('UserLogout/',views.UserLogout,name="UserLogout"),
path('save_cart/',views.save_cart,name="save_cart"),
path('cart_page/',views.cart_page,name="cart_page"),
path('delete_item/<int:P_id>',views.delete_item,name="delete_item"),
path('user_login_page/',views.user_login_page,name="user_login_page"),
path('checkout_page/',views.checkout_page,name="checkout_page"),
path('payment_page/',views.payment_page,name="payment_page"),
path('save_checkout/',views.save_checkout,name="save_checkout"),

]