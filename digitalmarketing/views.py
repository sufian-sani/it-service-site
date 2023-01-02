from django.shortcuts import render
from .models import *
from mainapp.models import *

# Create your views here.
def seo_service_details(request):
    seoservicehomepagecontentandmeta=Seoservicehomepagecontentandmeta.objects.first()
    # seopagefirstsection = Seopagefirstsection.objects.first()
    seopagebenefits = Seopagebenefits.objects.all()[:4]
    seoservicefaq = Seoservicefaq.objects.all()
    seoportfolio = Seoportfolio.objects.all()

    # seoservicehomepagemeta = Seoservicehomepagemeta.objects.first()

    pricingcard = Pricingcard.objects.all()
    pricingattibute = Pricingattibute.objects.all()

    serviceselect = Serviceselect.objects.first()

    seo_pricingcard_ls = []
    
    for i in pricingcard:
        if i.catagory == serviceselect.serviceselect:
            seo_pricingcard_ls.append(i)

    pricingcard = seo_pricingcard_ls



    context = {
        'seoservicehomepagecontentandmeta': seoservicehomepagecontentandmeta,
        # 'seopagefirstsection': seopagefirstsection,
        'seopagebenefits': seopagebenefits,
        'seoservicefaq': seoservicefaq,
        'seoportfolio': seoportfolio,
        'pricingcard':pricingcard,
        'pricingattibute':pricingattibute,
        # 'meta':seoservicehomepagemeta,
    }
    return render(request, 'digitalmarketing/seo-service-details.html',context)

def protfolio_details(request, slug):
    seoportfolio=Seoportfolio.objects.get(slug=slug)
    # seoportfoliopagemeta=Seoportfoliopagemeta.objects.first()
    portfolio_details_img = PortfolioImage.objects.filter(portfolio=seoportfolio).values('images')
    context = {
        'seoportfolio': seoportfolio,
        'portfolio_details_img':portfolio_details_img,
        # 'meta':seoportfoliopagemeta,
    }
    return render(request, 'digitalmarketing/protfolio-details.html',context)