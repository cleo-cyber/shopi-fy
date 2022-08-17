
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('email required')
        if not username:
            raise ValueError('username required')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, default='')
    username = models.CharField(
        verbose_name='username', max_length=100, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, obj=None):
        return True

    def has_module_perms(self, app_label):
        return self.is_superuser


class Tracks(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    track_banner = models.ImageField(
        null=True, blank=True, upload_to='trackImages/')
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Tour(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    event_description = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event_type = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.venue

    class Meta:
        ordering = ['created']
