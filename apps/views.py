from django.shortcuts import render,HttpResponse,get_object_or_404
from django.db.models import Count, Avg
from apps.models import Product, Category ,Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Adress
from taggit.models import Tag
def index(request):
    #products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published",featured=True)

    context = {
        "products":products
    }
    return render(request, 'apps/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {
        "products":products
    }
    return render(request, 'apps/products-list.html', context)
def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }
    return render(request, 'apps/category-list.html',context)

def category_product_list_view(request,cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published",category=category)
    context = {
        "category":category,
        "products":products,
    }
    return render(request, "apps/category-product-list.html", context)

def vendor_list_view(request):
    vendor = Vendor.objects.all()

    context = {
        "vendor":vendor,
    }
    return render(request, "apps/vendor-list.html", context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")
    context = {
        "vendor": vendor,
        "products": products,

    }
    return render(request, "apps/vendor-detail.html", context)
def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)

    reviews = ProductReview.objects.filter(product=product).order_by("-date")
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    p_image = product.p_images.all()
    products = Product.objects.filter(category=product.category).exclude(pid=pid)
    #product = get_object_or_404(Product, pid=pid)
    context = {
        "p":product,
        "p_image":p_image,
        "average_rating":average_rating,
        "reviews":reviews,
        "products":products
    }
    return render(request, "apps/product-detail.html", context)
def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products":products,
        "tag":tag
    }

    return render(request, "apps/tag.html", context)
