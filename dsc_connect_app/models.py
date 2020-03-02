import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

STATUS_CHOICES = [
	('0','draft'),
	('1','published'),
	]


class Dsc(models.Model):
	
	
	author = models.ForeignKey('User', on_delete=models.CASCADE)
	status = models.CharField(max_length=1, choices = STATUS_CHOICES, default = STATUS_CHOICES[0][1])
	lead = models.CharField(max_length = 256 , blank = False)
	name = models.CharField(max_length=50)
	quote = models.CharField(max_length = 512)
	domains =ArrayField(models.CharField(max_length = 512, blank = True))
	gmail = models.EmailField(blank=True)
	city = models.CharField(max_length=300)
	state = models.CharField(max_length=300)
	country = models.CharField(max_length=256)
	team_size = models.IntegerField()
	established_on =models.DateField(auto_now=False)
	created_on = models.DateTimeField(auto_now_add=False)
	updated_on = models.DateTimeField(auto_now=True)
	website = models.URLField(blank=True)
	github = models.URLField(blank=True)
	medium = models.URLField(blank=True)
	facebook = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	linkedin = models.URLField(blank=True)
	instagram = models.URLField(blank=True)
	youtube = models.URLField(blank=True)
	behance = models.URLField(blank=True)
	custom = ArrayField(models.URLField(blank=True))
	"""
		add fields here!!
	"""


	def __str__(self):
		return self.name




class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model to implement login with phone_number and password
    """
    email = models.EmailField(_('email address'), blank=True, unique = True)
    phone_number = models.CharField(_('phone number'), max_length=10, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    gender = models.CharField(_('gender'), max_length=8, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(_('admin'), default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_worker = models.BooleanField(_('worker'), default=False)
    is_volunteer = models.BooleanField(_('volunteer'), default=False)
    is_online = models.BooleanField(_('online'), default=False)
    last_activity = models.DateTimeField(_('last activity'), default=datetime.date.today)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    otp = models.CharField(max_length=4, null=False, blank=False, default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    