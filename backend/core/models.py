from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 100)
    is_vendor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')
    bio = models.TextField()
    contact_details = models.TextField()
    bank_details = models.TextField()
    shipping_policy = models.TextField()
    return_policy = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length= 100)
    slug = models.SlugField(max_length= 100, unique = True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True,related_name='subcategories')


    def __str__(self):
        return self.name
    
class Product(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name='product')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits = 100, decimal_places=2)
    stock = models.PositiveIntegerField()
    images = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'orders')
    products = models.ManyToManyField(Product,through='OrderItem')
    total_price = models.DecimalField(max_digits= 100, decimal_places=2)
    shipping_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'cart', null=True, blank=True)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    items = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    user = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name = 'items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)


class Shipping(models.Model):
    name = models.CharField(max_length=  100)
    description = models.TextField()
    rate = models.DecimalField(max_digits= 10, decimal_places=  2)

class Payment (models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE,related_name="payments")
    method = models.CharField (max_length= 100)
    amount = models.DecimalField (max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Coupon (models.Model):
    code = models.CharField(max_length=100, unique=True)
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name=  "reviews")
    customer = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product,related_name='whishlists')

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Blog(models.Model):
    title = models.CharField(max_length= 200)
    slug = models.SlugField(max_length=100,unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FAQ(models.Model):
    question = models.TextField()
    answers = models.TextField()

class Analytics(models.Model):
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    traffic = models.PositiveIntegerField()
    popular_products = models.ManyToManyField(Product, related_name='analytics')
    created_at = models.DateTimeField(auto_now_add=True)
    

class Configuration(models.Model):
    site_name = models.CharField(max_length= 100)
    site_description = models.TextField()
    site_logo = models.ImageField(upload_to='logos')

class Tax(models.Model):
    name = models.CharField(max_length = 100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True,blank=True)

    
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    Subscribed_at = models.DateField(auto_now_add=True)
    

class Refund(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='refunds')
    reason = models.TextField()
    amount = models.DecimalField(max_digits = 5, decimal_places = 2)
    status = models.CharField(max_length=100)
    requested_at = models.DateTimeField(auto_now_add= True)
    processed_at = models.DateTimeField(null = True, blank=True)



