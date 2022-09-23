# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse


from django.contrib import sitemaps
from django.urls import reverse

from digitalmarketing.models import *

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['mainapp:index', 'mainapp:faq','mainapp:services_page','mainapp:startupdetails','digitalmarketing:seo_service_details']

    def location(self, item):
        return reverse(item)


class PostSitemap(sitemaps.Sitemap):
	changegreq = 'weekly'
	priority = 0.9
	def items(self):
		return Seoportfolio.objects.all()

	def location(self, item):
		return item.get_absolute_url()

	# def lastmod(self, obj):
	# 	return obj.updated


# from mainapp import views

# class Static_Sitemap(Sitemap):

#     priority = 1.0
#     changefreq = 'yearly'

#     def items(self):
#         return ['index', 'faq','services_page','startupdetails','seo_service_details','protfolio_details']

#     def location(self, item):
#         return reverse(item)


# from django.contrib.sitemaps import Sitemap

# from mainapp.models import *
# from digitalmarketing.models import *

# class PostSitemap(Sitemap):
# 	changegreq = 'weekly'
# 	priority = 0.9
# 	def items(self):
		# context['homepagemeta'] = Homepagemeta.objects.filter(status='published')
		# context['headerhomepage'] = Headerhomepage.objects.filter(status='published')
		# context['startuppagemeta'] = Startuppagemeta.objects.filter(status='published')
		# context['startupsection'] = Startupsection.objects.filter(status='published')
		# context['startupdetails'] = Startupdetails.objects.filter(status='published')
		# context['teampagemeta'] = Teampagemeta.objects.filter(status='published')
		# context['teampagesubtitle'] = Teampagesubtitle.objects.filter(status='published')
		# context['teampage'] = Teampage.objects.filter(status='published')
		# context['servicepagemeta'] = Servicepagemeta.objects.filter(status='published')
		# context['servicepagesubtitle'] = Servicepagesubtitle.objects.filter(status='published')
		# context['seoservicehomepagemeta'] = Seoservicehomepagemeta.objects.filter(status='published')
		# context['seopagesubtitle'] = Seopagesubtitle.objects.filter(status='published')
		# context['seopagefirstsection'] = Seopagefirstsection.objects.filter(status='published')
		# context['seoportfoliopagemeta'] = Seoportfoliopagemeta.objects.filter(status='published')
		# context['seoportfolio'] = Seoportfolio.objects.filter(status='published')
		# context['portfolioImage'] = PortfolioImage.objects.filter(status='published')

	# 	return Headerhomepage.objects.filter(status='published')

	# def lastmod(self, obj):
	# 	return obj.updated