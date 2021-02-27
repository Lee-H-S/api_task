from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, email, account_type, password=None, **extra_fields):
        """
        Creates and saves a new user
        """
        user = self.model(email=email, account_type=account_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a new superuser
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AccountType(models.Model):
    """
    Account Type Model: Used to determine permissions
    """

    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    """
    User Model: Used to create users in the DB
    """

    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=256, unique=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    active_flag = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    closed_date = models.DateField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["account_type", "display_name"]

    def __str__(self):
        return self.email


class Game(models.Model):
    """
    Game Model: Used to create games in the DB
    """

    title = models.CharField(max_length=256, unique=True)
    studio = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    """
    Subscription Model: Used to create subscriptions in the DB
    """

    player = models.ForeignKey(User, on_delete=models.PROTECT)
    game = models.OneToOneField(Game, on_delete=models.PROTECT)
    active_flag = models.BooleanField(default=True)
    subscription_date = models.DateField(auto_now_add=True)
    cancellation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.player} -> {self.game}"
