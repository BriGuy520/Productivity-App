from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.

class DoerManager(BaseUserManager):

  def create_user(self, email, first_name, last_name, password=None, commit=True):

    if not email:
      raise ValueError(_('Doers must have an email address'))
    if not first_name:
      raise ValueError(_('Doers must have a first name'))
    if not last_name:
      raise ValueError(_('Doers must have a last name'))

    doer = self.model(
      email=self.normalize_email(email),
      first_name=first_name,
      last_name=last_name,
    )

    doer.set_password(password)
    
    if commit:
      doer.save(using=self._db)
    return doer

  def create_superuser(self, email, first_name, last_name, password):

    user = self.create_user(
      email, 
      password=password,
      first_name=first_name,
      last_name=last_name,
      commit=False,
    )

    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


class Doer(AbstractBaseUser, PermissionsMixin):
  
  email = models.EmailField(
    verbose_name=_('email address'), max_length=255, unique=True
  )

  first_name = models.CharField(_('first_name'), max_length=24, blank=True)
  last_name = models.CharField(_('last_name'), max_length=100, blank=True)

  is_active = models.BooleanField(
    _('active'),
    default=True,
    help_text= _(
      'Designates whether this user should be treated as active. '
      'Unselect this instead of deleting accounts.'
    ),
  )

  is_staff = models.BooleanField(
    _('staff status'),
    default=False,
    help_text = _(
      'Designates whether the user can log into the admin'
    )
  )

  date_joined = models.DateTimeField(
    _('date joined'), default=timezone.now
  )

  objects = DoerManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  def get_full_name(self):

    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()


  def __str__(self):
    return '{} <{}>'.format(self.get_full_name, self.email)
  
  def has_perm(self, perm, obj=None):

    return True
  
  def has_module_perms(self, app_label):

    return True



