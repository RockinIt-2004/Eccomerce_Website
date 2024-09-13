from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.db.models import Count, Avg
from apps.models import Product, Category ,Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Adress
from taggit.models import Tag
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
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
    vendors = Vendor.objects.all()

    context = {
        "vendors":vendors,
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
def search_view(request):
    query = request.GET.get("q")
    products = Product.objects.filter(title__icontains=query).order_by("-date")

    context = {
        "products":products,
        "query": query,
    }
    return render(request, "apps/search.html" , context)

def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid']
    }

    if 'cart_data_obj' in request.session:
       if str(request.GET['id']) in request.session['cart_data_obj']:
           cart_data =  request.session['cart_data_obj']
           cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
           cart_data.update(cart_data)
           request.session['cart_data_obj'] = cart_data
       else:
           cart_data = request.session['cart_data_obj']
           cart_data.update(cart_product)
           request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})

def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "apps/cart.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    else:
        messages.warning(request, "Your cart is empty")
        return redirect("apps:index")

def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_obj_data'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
    context = render_to_string("apps/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})



def update_cart(request):
    product_id = str(request.GET['id'])
    product_qty = request.GET['qty'] 
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = product_qty
            request.session['cart_obj_data'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
    context = render_to_string("apps/async/cart-list.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})


def checkout_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "apps/checkout.html", {"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})

