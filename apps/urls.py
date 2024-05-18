from django.urls import path
from apps.views import index,product_list_view,category_list_view,category_product_list_view, vendor_list_view,vendor_detail_view,product_detail_view,tag_list
app_name="apps"
urlpatterns = [
    #Homepage
    path("",index,name="index"),
    #products
    path("products/", product_list_view, name="products-list"),
    path("product/<pid>", product_detail_view, name="product-detail"),

    #category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),
    #vendor
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>", vendor_detail_view, name="vendor-detail"),
    #tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags")
]