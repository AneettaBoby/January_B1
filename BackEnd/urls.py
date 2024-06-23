from django.urls import path
from BackEnd import views


urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('categories_page/',views.categories_page,name="categories_page"),
    path('save_categories/', views.save_categories, name="save_categories"),
    path('display_category/', views.display_category, name="display_category"),
    path('Edit_page/<int:e_id>',views.Edit_page,name="Edit_page"),
    path('Update_image/<int:e_id>', views.Update_image, name="Update_image"),
    path('delete_page/<int:e_id>', views.delete_page, name="delete_page"),
    path('login_page/',views.login_page,name="login_page"),
    path('adminLogin/',views.adminLogin,name="adminLogin"),
    path('Product_page/',views.Product_page,name="Product_page"),
    path('save_products/',views.save_products,name="save_products"),
    path('display_product/',views.display_product,name="display_product"),
    path('Edit_product/<int:pro_id>',views.Edit_product,name="Edit_product"),
    path('Update_ProductImage/<int:pro_id>',views.Update_ProductImage,name="Update_ProductImage"),
path('contact_details/',views.contact_details,name="contact_details"),


]

