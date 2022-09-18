from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField

from django.core.validators import RegexValidator

from mainapp.models import Servicesection
# Create your models here.

# seo model start

class Seoservicehomepagemeta(models.Model):
    site_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.site_title

    class Meta: 
        verbose_name = "SEO Service Page Meta - SEO Homepage"
        verbose_name_plural = "SEO Service Page Meta - SEO Homepage"

class Serviceselect(models.Model):
    serviceselect = models.ForeignKey(Servicesection, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.serviceselect)

    class Meta: 
        verbose_name = "Service Select - SEO Page"
        verbose_name_plural = "Service Select - SEO Page"

class Seopagesubtitle(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Header - SEO Page"
        verbose_name_plural = "Header - SEO Page"

class Seopagefirstsection(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField(config_name='basic_ckeditor',blank=True,null=True)
    image = models.ImageField(upload_to='aboutus')
    img_alt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "First Section - Seo Page"
        verbose_name_plural = "First Section - Seo Page"

class Seopagebenefits(models.Model):
    icon_class = models.CharField(max_length=500)
    bd_coloer = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Benefits - Seo Page"
        verbose_name_plural = "Benefits - Seo Page"

class Seoservicefaq(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField(config_name='basic_ckeditor',blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Faq - Seo Page"
        verbose_name_plural = "Faq - Seo Page"

class Seoportfoliopagemeta(models.Model):
    site_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.site_title

    class Meta: 
        verbose_name = "SEO Portfolio Page Meta - SEO Homepage"
        verbose_name_plural = "SEO Portfolio Page Meta - SEO Homepage"

class Seoportfolio(models.Model):
    title = models.CharField(max_length=500)
    feature_image = models.ImageField(upload_to='seoportfolio/')
    img_alt = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Portfolio - Seo Page"
        verbose_name_plural = "Portfolio - Seo Page"


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Seoportfolio, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'seoportfolio/',  blank=True, null=True)
    img_alt = models.CharField(max_length=200, blank=True, null=True)


# seo model end
