from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyManager(BaseUserManager):
    def create_user(self, email,password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password =password
        )
        print("this is pass -------",password)
        user.set_password(password)
    
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    username =models.CharField(max_length=25,null=True,blank=True,default=None)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now=True)
    is_varified  = models.BooleanField(default=False)
    email_token = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    password = models.CharField(max_length=255)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS= []  
    
    objects = MyManager()
    
    def  __str__(self):
        return self.email


    def get_fullname(self):
        return self.fullname
    
    def  get_short_name(self):
        return self.email


    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_active(self):
        return self.active
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    
   



class CreateInvoice(models.Model):
    brandname =models.CharField(max_length=100)
    date = models.DateTimeField(blank=True ,null=True)
    send_usermail = models.EmailField(unique=True)
    reciver_usermail = models.EmailField(unique=True) 
    invoiceno = models.CharField(max_length=21)
    item_description =models.TextField()
    price = models.FloatField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    subtotal = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name="Invoice_User" , null = True, blank=True)
 

class SendInvoice(models.Model):
    pass
    # Title = 
    # to = 
    # sendermail=
    # user = models.ForeignKey(User,on_delete=models.CASCADE , related_name="SendUser" , null = True, blank=True)
 



    
































# class MyManager(BaseUserManager):
#     use_in_migrations = True
#     def create_user(self,email,password=None,is_active=True,is_staff=None,is_admin=None):
#         if not email:
#             raise ValueError("User must have email address")

#         if not password:
#             raise ValueError("User must have Password")
#         user_obj = self.model(
#             email= self.normalize_email(email)
#         )
#         user_obj.set_password(password)
#         user_obj.staff= is_staff
#         user_obj.admin = is_admin
#         user_obj.active = is_active
#         user_obj.save(using=self._db)
#         return user_obj

#     def create_staffuser(self,email,password=None,):
#         user =self.create_user(email,password=password,is_staff=True,
#         )
#         return user

#     def create_superuser(self,email,password=None):
#         user =self.create_user(email,password=password,is_staff=True,
#                 is_admin=True,is_active=True
#         )
#         return user