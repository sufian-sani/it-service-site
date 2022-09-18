from turtle import color
from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField

from django.core.validators import RegexValidator
# Create your models here.

# seo section start

class Homepagemeta(models.Model):
    site_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.site_title

    class Meta: 
        verbose_name = "Homepage Meta - Homepage"
        verbose_name_plural = "Homepage Meta - Homepage"

# seo section end

# index page start
class Headerhomepage(models.Model):
    subtitle = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    sort_description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='header_homepage')
    img_alt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Header - Homepage"
        verbose_name_plural = "Header - Homepage"

class Startuppagemeta(models.Model):
    site_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.site_title

    class Meta: 
        verbose_name = "Startup Meta - Start up Page"
        verbose_name_plural = "Startup Meta - Start up Page"

class Startupsection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='startup_section')
    img_alt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Startup - Homepage"
        verbose_name_plural = "Startup - Homepage"

class Startupdetails(models.Model):
    sub_title = models.CharField(max_length=500)
    body_description = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.sub_title

    class Meta: 
        verbose_name = "Startup Details Page - Homepage Startup"
        verbose_name_plural = "Startup Details Page - Homepage Startup"

class Testimonialsection(models.Model):
    short_speech = models.TextField()
    image = models.ImageField(upload_to='testimonial_section')
    img_alt = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100)
    organigation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Testimonial - Homepage"
        verbose_name_plural = "Testimonial - Homepage"

class Counterbar(models.Model):
    achievement_title = models.CharField(max_length=100)
    achievement_award = models.IntegerField(default=0)

    def __str__(self):
        return self.achievement_title

    class Meta: 
        verbose_name = "Counter Bar - Homepage"
        verbose_name_plural = "Counter Bar - Homepage"

class Contactussection(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    phone = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list

    def __str__(self):
        return str('Phone Number')

    class Meta: 
        verbose_name = "Contact-us - Homepage"
        verbose_name_plural = "Contact-us - Homepage"

class Footersection(models.Model):
    footer_main_description = models.TextField()
    newsletter_description = models.CharField(max_length=500)

    def __str__(self):
        return str('Footer Section Text')

    class Meta: 
        verbose_name = "Footer - Homepage"
        verbose_name_plural = "Footer - Homepage"


class Servicesection(models.Model):
    icon = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service_page', blank=True, null=True)
    img_alt = models.CharField(max_length=200, blank=True, null=True)
    colour = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Service - Homepage"
        verbose_name_plural = "Service - Homepage"


# index page end

#about us page start

class Aboutuspagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('About Page Subtitle')

    class Meta: 
        verbose_name = "Subtitle - About Page"
        verbose_name_plural = "Subtitle - About Page"

class Aboutusfirstsection(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField(config_name='basic_ckeditor',blank=True,null=True)
    image = models.ImageField(upload_to='aboutus')
    img_alt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "First Section - About Page"
        verbose_name_plural = "First Section - About Page"

class Aboutussecondsection(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField(config_name='basic_ckeditor',blank=True,null=True)
    image = models.ImageField(upload_to='aboutus')
    img_alt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Second Section - About Page"
        verbose_name_plural = "Second Section - About Page"

#about us page end


#faq page start

class Faqpagemeta(models.Model):
    site_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.site_title

    class Meta: 
        verbose_name = "Faq Meta - Faq Page"
        verbose_name_plural = "Faq Meta - Faq Page"

# meta

class Faqpagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('Faq Page Subtitle')

    class Meta: 
        verbose_name = "Subtitle - Faq Page"
        verbose_name_plural = "Subtitle - Faq Page"

class Faqpage(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField(config_name='basic_ckeditor',blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Faq - Faq Page"
        verbose_name_plural = "Faq - Faq Page"

#faq page end

#history page start

class Historypagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('History Page Subtitle')

    class Meta: 
        verbose_name = "Subtitle - History Page"
        verbose_name_plural = "Subtitle - History Page"

class Historysection(models.Model):
    image = models.ImageField(upload_to='historysection')
    year = models.IntegerField()
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "History - History Page"
        verbose_name_plural = "History - History Page"

#history page end

#Team page strat

class Teampagemeta(models.Model):
    site_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.site_title

    class Meta: 
        verbose_name = "Team Meta - Faq Page"
        verbose_name_plural = "Team Meta - Faq Page"

class Teampagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('Team Page Subtitle')

    class Meta: 
        verbose_name = "Subtitle - Team Page"
        verbose_name_plural = "Subtitle - Team Page"


class Teampage(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teampage')
    img_alt = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Team - Team Page"
        verbose_name_plural = "Team - Team Page"

#Team page end

#service page start

class Servicepagemeta(models.Model):
    site_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.site_title

    class Meta: 
        verbose_name = "Service Meta - Service Page"
        verbose_name_plural = "Service Meta - Service Page"

class Servicepagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('Service Page Subtitle')

    class Meta: 
        verbose_name = "Subtitle - Service Page"
        verbose_name_plural = "Subtitle - Service Page"

class Serviceskill(models.Model):
    title = models.CharField(max_length=200)
    skill_rate = models.IntegerField(help_text="give number 0 to 100, It's repreasent skill parcentage")

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Service Counter - Service Page"
        verbose_name_plural = "Service Counter - Service Page"

#service page end

#contact us page start

class Contactpagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('Contact Page Subtitle')

    class Meta: 
        verbose_name = "Subtitle - Contact Page"
        verbose_name_plural = "Subtitle - Contact Page"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Contact - Contactus Page"
        verbose_name_plural = "Contact - Contactus Page"

class Addresslocation(models.Model):
    office_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
    phone = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
    email = models.EmailField(max_length=100)
    colour = models.CharField(max_length=200)

    def __str__(self):
        return self.office_name

    class Meta: 
        verbose_name = "Address location - Contactus Page"
        verbose_name_plural = "Address location - Contactus Page"

#contact us page end

#pricing us page start

class Pricingpagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('Pricing Page Subtitle')

    class Meta: 
        verbose_name = "Subtitle - Pricing Page"
        verbose_name_plural = "Subtitle - Pricing Page"

class Pricingcard(models.Model):
    catagory = models.ForeignKey(Servicesection, on_delete=models.CASCADE, related_name="pricing")
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    sub_title = models.CharField(max_length=500)
    highlight_colour = models.CharField(max_length=200, default='#5b84f8')
    monthly_prices = models.DecimalField(max_digits=5,decimal_places=2)
    yearly_prices = models.DecimalField(max_digits=5,decimal_places=2)
    show_on_homepage = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title + ' - ' + str(self.catagory)

    class Meta: 
        verbose_name = "Pricing Plan - Pricing Page"
        verbose_name_plural = "Pricing Plan - Pricing Page"

class Pricingattibute(models.Model):
    catagory = models.ForeignKey(Pricingcard, on_delete=models.CASCADE, related_name="pricing_attibute")
    attibute = models.CharField(max_length=500)

    def __str__(self):
        return self.attibute

    class Meta: 
        verbose_name = "Pricing Attibute - Pricing Page"
        verbose_name_plural = "Pricing Attibute - Pricing Page"

#pricing us page end

# pricing Subscribe start

class Pricingsubscribe(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    url = models.URLField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    package_type = models.CharField(max_length=300)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Pricing Subscribe"
        verbose_name_plural = "Pricing Subscribe"

# pricing Subscribe end

# privacy policy start

class Privacypolicypagesubtitle(models.Model):
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return str('Privacy Policy Subtitle')

    class Meta: 
        verbose_name = "Subtitle - Privacy Policy Page"
        verbose_name_plural = "Subtitle - Privacy Policy Page"

class Privacypolicybody(models.Model):
    body_description = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return str('Privacy policy body description')

    class Meta: 
        verbose_name = "Body Description - Privacy Policy Page"
        verbose_name_plural = "Body Description - Privacy Policy Page"


# privacy policy end





