from django.contrib import admin
from .models import *
# Register your models here.

# seo start

admin.site.register(Seoservicehomepagemeta)
admin.site.register(Serviceselect)
admin.site.register(Seopagesubtitle)
admin.site.register(Seopagefirstsection)
admin.site.register(Seopagebenefits)
admin.site.register(Seoservicefaq)


admin.site.register(Seoportfoliopagemeta)


class ProtfolioImageAdmin(admin.StackedInline):
    model = PortfolioImage
 
@admin.register(Seoportfolio)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProtfolioImageAdmin]
 
    class Meta:
       model = Seoportfolio

# seo end
