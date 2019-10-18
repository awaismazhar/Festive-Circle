from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    
    #creates user with given email and password
    def create_user(self, email, name, dob, pfp, address, about_me, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            dob=dob,
            pfp=pfp,
            address=address,
            about_me=about_me,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    #creates staffuser with given email and password
    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            name="admin",
            dob= None, 
            pfp="none", 
            address="none", 
            about_me="none"
        )
        user.staff = True
        user.save(using=self._db)
        return user

    
    #creates superuser with given email and password
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            name="admin",
            dob= None, 
            pfp="none", 
            address="none", 
            about_me="none"
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name    =   'email address',
        max_length      =   255,
        unique          =   True,
    )
    active  =   models.BooleanField(default = True)  #false when user deletes his account
    staff   =   models.BooleanField(default = False) #an admin user; non super-user
    admin   =   models.BooleanField(default = False) #a superuser
    
    # extended
    name = models.CharField(
        max_length = 100, 
        blank = True, 
        null = True
    )
    dob = models.DateField(
        blank = True, 
        null = True
    )
    
    pfp = models.ImageField(
        upload_to="images/",
    )

    address = models.CharField(
        max_length = 255, 
        blank = True, 
        null = True
    )
    about_me = models.CharField(
        max_length = 255, 
        blank = True, 
        null = True
    )    
    #password field is not requited as it's built in

    USERNAME_FIELD = 'email' #makes email the default username fielf
    REQUIRED_FIELDS = [] #email & password are required by default.

    objects = UserManager() #setting up user manager

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):              
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    # def save(self, *args, **kwa):
    #     print("hereherehereherehere")
        
class Visitors(models.Model):
    ip_address = models.GenericIPAddressField(blank = False)
    time_stamp = models.DateTimeField(auto_now_add = True)
    frequency  = models.BigIntegerField(default=1)

class reset_codes(models.Model):
    user = models.OneToOneField(
                    User, related_name='pass_reset', 
                    on_delete=models.CASCADE
                    )
    code =  models.CharField(max_length=4)
    time_stamp = models.DateTimeField(auto_now_add=True)

