# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Min
from django.forms.utils import ErrorList 
from wagtail.wagtailadmin import messages
from wagtail.wagtailadmin.edit_handlers import (TabbedInterface, ObjectList,
                                                PageChooserPanel, FieldPanel,
                                                InlinePanel, MultiFieldPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey

class Category(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    intro = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def get_children_categories(self):
        return self.get_children().type(Category).live().in_menu()
       
    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
    ]

    subpage_types = ['products.Category', 'products.Product']
    parent_page_types = ['products.Category', 'main.MerchantPage']



class Feature(models.Model):
    name = models.CharField('Nombre', max_length=15)
    
    class Meta:
        verbose_name = "Característica"
        verbose_name_plural = "Características"

    def __str__(self):
        return self.name

class Picture(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        ImageChooserPanel('image'),
    ]


class ProductPicture(Orderable, Picture):
    page = ParentalKey('products.Product', related_name='pictures')

class Variant(models.Model):
    feature = models.ForeignKey(
        Feature,
        null=True,
        blank=True,
        help_text="Características para esta referencia. Ejemplo: Color"
    )
    value = models.CharField(
        'Valor de característica',
        max_length=200,
        null=True,
        blank=True,
        help_text="Ejemplo: Si tu característica es 'Color', valor podría ser 'Verde'"
    )
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    on_discount = models.BooleanField(
        'En oferta',
        default=False,
        help_text="Activa esta opción si esta referencia está en oferta"
    )
    discount_percentage = models.PositiveIntegerField(
        'Porcentaje de descuento',
        null=True,
        blank=True,
        help_text="Si esta referencia está en oferta, ingresa el porcentaje de descuento"
    )
    product = ParentalKey('products.Product', related_name='variants')
    stock_quantity = models.IntegerField('Cantidad de stock')

    class Meta:
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"

    def __str__(self):
        return self.name

    def get_stock(self):
        return self.stock
    
    def on_discount(self):
        if discount_percentage is not None:
            return True
        else:
            return False

    def clean(self):
        #Validate if there is feature but not value and viceversa
        if self.feature and not self.value:
            raise ValidationError({
                'value': ValidationError('Asignale un valor a cada característica de tu referencia de producto. Ej: Verde', code='not_allowed'),
            })
        if self.value and not self.feature:
            raise ValidationError({
                'feature': ValidationError('Selecciona una característica para tu referencia de producto. Ej: Color', code='not_allowed'),
            })
        
        #Validate if discount percentage is zero to override it to null as integrity requires it
        if self.discount_percentage == 0:
            self.discount_percentage = None
            

class Product(Page):
    description = RichTextField('Descripcion', help_text="Describe tu producto al público")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def get_price(self):
        minor_price_variant = self.get_variants().aggregate(Min('price'))
        return minor_price_variant['price__min']
    
    def get_variants(self):
        return Variant.objects.filter(product=self)

    def __str__(self):
        return self.name

    content_panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        InlinePanel('pictures', label='Imagenes')
    ]
    variant_panels = [
        InlinePanel('variants', label='Referencias')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Producto'),
        ObjectList(variant_panels, heading='Referencias'),
        ObjectList(Page.promote_panels, heading='SEO')
    ])

    search_fields = Page.search_fields + [
        index.SearchField('title'),
    ]

    subpage_types = []