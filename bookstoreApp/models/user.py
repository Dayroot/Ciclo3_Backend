from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .employee import Employee


class UserManager(BaseUserManager):
    
    def create_user(self,username, password=None):
        
        if not username:
            raise ValueError('Users must have an username')
        user= self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, password):
        user = self.create_user(
            username = username,
            password = password
        )
        user.is_admin= True
        user.save(using=self._db)
        return user
    
    def create_employee(self,
                        username, 
                        password, 
                        work_area, 
                        salary, 
                        is_seller=False, 
                        is_inventory_manager=False, 
                        is_admin=False
                        ):
        
        user= self.create_user(username=username, password=password)
        user.is_employee= True
        user.save(using=self._db)
        
        Employee.objects.create(
            user=user,
            work_area=work_area,
            salary= salary,
            is_seller= is_seller,
            is_inventory_manager=is_inventory_manager,
            is_admin= is_admin
            )
        return user

    def create_client(self,username, password):
        user= self.create_user(username=username, password=password)
        user.is_client= True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_FEMALE= 'F'
    GENDER_MALE ='M'
    GENDER_UNSURE= 'U'
    
    GENDER_CHOISES = (
        (GENDER_FEMALE,'Female'),
        (GENDER_MALE, 'Male'),
        (GENDER_UNSURE, 'Unsure')
     )
    
    username= models.CharField('Username', max_length=15, unique=True)
    password= models.CharField('Password', max_length=256)
    fullname= models.CharField('Fullname', max_length=200, blank=True, null=True)
    datebirth = models.DateField('Datebirth', blank=True, null=True)
    gender = models.CharField(max_length=1, choices= GENDER_CHOISES, default=GENDER_UNSURE)
    email = models.EmailField('Email', max_length=320, blank=True, null=True)
    identification= models.CharField('Identification', max_length=15, blank=True, null=True)
    phone_number = models.CharField('Phone number',max_length=15, blank=True, null=True)
    address = models.CharField('Address', max_length=50,blank=True, null=True)
    is_employee= models.BooleanField(default=False)
    is_client= models.BooleanField(default=False)
    
    def save(self, **kwargs):
        some_salt= 'JK0Xh1i69jxdr5YdJkP'
        self.password= make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD= 'username'
    EMAIL_FIELD= 'email'
    
