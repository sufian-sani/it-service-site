from django.contrib import admin
from .models import *
# Register your models here.

# home page start
admin.site.register(Headerhomepage)
admin.site.register(Startupsection)
admin.site.register(Testimonialsection)
admin.site.register(Contactussection)
admin.site.register(Footersection)
admin.site.register(Servicesection)
admin.site.register(Counterbar)
admin.site.register(Homepagemeta)


admin.site.register(Startuppagemeta)

# home page end


# about us page start
admin.site.register(Aboutuspagesubtitle)
admin.site.register(Aboutusfirstsection)
admin.site.register(Aboutussecondsection)


# about us page end

# faq page start

admin.site.register(Faqpagemeta)
admin.site.register(Faqpagesubtitle)
admin.site.register(Faqpage)

# faq page end

# history page start

admin.site.register(Historypagesubtitle)
admin.site.register(Historysection)

# history page end

# team page start

admin.site.register(Teampagemeta)
admin.site.register(Teampagesubtitle)
admin.site.register(Teampage)

# team page end

# service page start
admin.site.register(Servicepagemeta)
admin.site.register(Servicepagesubtitle)
admin.site.register(Serviceskill)

# service page end

# contactus page start

class ContactPageAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'message','date_time']

admin.site.register(Contact,ContactPageAdmin)
admin.site.register(Addresslocation)

# contactus page end

# pricing page start

admin.site.register(Pricingpagesubtitle)
admin.site.register(Pricingcard)
admin.site.register(Pricingattibute)

# pricing page end

# pricing Subscribe start

admin.site.register(Pricingsubscribe)

# pricing Subscribe end

# privacy policy start

admin.site.register(Privacypolicypagesubtitle)
admin.site.register(Privacypolicybody)
admin.site.register(Startupdetails)

# privacy policy end
