from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# class Menu(models.Model):
#     name = models.CharField(max_length=24, unique=True, verbose_name='menu name')
#     slug = models.SlugField(max_length=24, unique=True)
#     additional_text = models.CharField(max_length=128, null=True,blank=True)
#     order = models.PositiveSmallIntegerField(default=0)
#
#     class Meta:
#
#         ordering = ['order']

# class MenuCategory(models.Model):
#     menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
#     name = models.CharField(max_length=32, verbose_name='menu category name')
#     additional_text = models.CharField(max_length=128, null=True, blank=True)
#     order = models.IntegerField(default=0)
#
#     class Meta:
#         verbose_name='menu category'
#         verbose_name_plural='menu catagories'
#         ordering = ['name', 'order']

    # def __unicode__(self):
    #     return self.name

class MenuItem(models.Model):
    CLASSIFICATION_CHOICES = (
        ('neither', 'Neither'),
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
    )

    name = models.CharField(max_length=48, help_text='Name of the item on the menu.')
    description = models.CharField(max_length=128, null=True, blank=True, help_text='Description of a menu item.')
    # category = models.ManyToManyField(MenuCategory, verbose_name='menu category', help_text='Category is the menu category that this menu item belongs to, i.e. \'Appetizers\'.')
    # order = models.IntergerField(default=0, verbose_name='order', help_text='The order is to specify the order in which items show on the menu')
    price = models.IntegerField(help_text='The price in the cost of the item.')

    # image = models.ImageField(upload_to='menu', null=True, blank=True,verbose_name='image', help_text='The image is an optional field that is associated with each menu item.')

    classification = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICES, default=0, verbose_name='classification', help_text='Select if this item classifies as Vegetarian, Vegan, or Neither.')
	# spicy = models.BooleanField(default=False, verbose_name='spicy?', help_text='Is this item spicy?')
	# contains_peanuts = models.BooleanField(default=True, verbose_name='contain peanuts?', help_text='Does this item contain peanuts?')
	# gluten_free = models.BooleanField(default=False, verbose_name='gluten free?', help_text='Is this item Gluten Free?')

    class Meta:
        verbose_name='menu item'
        verbose_name_plural='menu items'
        # ordering = ['category', 'order', 'name']
        # ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-wiki-page). """
        path_components = {'slug': self.slug}
        return reverse('menu-list', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)

        # Call save on the superclass.
        return super(MenuItem, self).save(*args, **kwargs)

        # def __unicode__(self):
    #     return self.name
