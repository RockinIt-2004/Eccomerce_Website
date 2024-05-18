from apps.models import Product, Category ,Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist, Adress


def default(request):
    categories = Category.objects.all()
    try:
        address = Adress.objects.get(user=request.user)
    except:
        adress = None
    return{
        'categories':categories
    }