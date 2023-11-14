from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        User,PermissionsMixin,
                                        BaseUserManager)
from django.forms import ValidationError
from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,name,password,address,date_of_birth):
        if not email:
            raise ValidationError("Email is required")
        if not name:
            raise ValidationError("name is required")
        if not password:
            raise ValidationError("password is required")
        
        user = self.model(email = email,name=name,address=address,date_of_birth=date_of_birth)
        user.is_active = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class Account(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateTimeField(null=True,blank=True)
    image = models.ImageField(upload_to="profile",null=True,blank=True,default='profile/pro.jpg')
    address = models.CharField(max_length=50,default='Kabul')


    is_staff = True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()

    class Meta:


        db_table = 'account'


class Junc(models.Model):
    user = models.ForeignKey(to= Account,on_delete=models.CASCADE,parent_link=False)
