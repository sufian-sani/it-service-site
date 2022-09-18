from django.shortcuts import render
from .models import *

from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    headerhomepage=Headerhomepage.objects.first()
    startupsection=Startupsection.objects.first()
    testimonialsection_all=Testimonialsection.objects.all()
    contactussection=Contactussection.objects.first()
    servicesection=Servicesection.objects.all()
    testimonialsection_all = Testimonialsection.objects.all()
    counterbar = Counterbar.objects.all()[:4]
    homepagemeta = Homepagemeta.objects.first()

    pricingcard = Pricingcard.objects.all()
    pricingattibute = Pricingattibute.objects.all()

    pricingcard_ls = []
    for i in pricingcard:
        if i.show_on_homepage == True:
            pricingcard_ls.append(i)

    pricingcard = pricingcard_ls


    if request.method=='POST':
        name=request.POST['name']
        email=request.POST.get('email', False)
        url=request.POST['url']
        address=request.POST.get('address', False);
        p_type=request.POST.get('p_type', False);
        
        subscribe=Pricingsubscribe(name=name, email=email, url=url, address=address, package_type=p_type)
        subscribe.save()

    # print(pricingcard)

    context = {
        'headerhomepage': headerhomepage,
        'startupsection':startupsection,
        'testimonialsection_all':testimonialsection_all,
        'contactussection':contactussection,
        'servicesection':servicesection,
        'pricingcard':pricingcard,
        'pricingattibute':pricingattibute,
        'counterbar':counterbar,
        'homepagemeta':homepagemeta,
    }
    return render(request, 'index.html',context)

def startupdetails(request):
    startupdetails = Startupdetails.objects.first()
    startuppagemeta = Startuppagemeta.objects.first()
    context = {
        'startupdetails':startupdetails,
        'meta':startuppagemeta,
    }
    return render(request, 'mainapp/statup-details.html',context)

def footernewsletter(request):
    if request.method=='POST':
        email=request.POST.get('email', False)
        print(email)

        return HttpResponseRedirect(reverse('mainapp:index'))
    return render(request, 'includes/footer.html')
    
def about_us(request):
    aboutuspagesubtitle=Aboutuspagesubtitle.objects.first()
    aboutusfirstsection=Aboutusfirstsection.objects.first()
    aboutussecondsection=Aboutussecondsection.objects.first()
    context = {
        'aboutuspagesubtitle': aboutuspagesubtitle,
        'aboutusfirstsection': aboutusfirstsection,
        'aboutussecondsection': aboutussecondsection,
    }
    return render(request, 'mainapp/about-us.html',context)

def our_team(request):
    teampagesubtitle=Teampagesubtitle.objects.first()
    teampage=Teampage.objects.all()
    teampagemeta = Teampagemeta.objects.first()
    context = {
        'teampagesubtitle': teampagesubtitle,
        'teampage':teampage,
        'meta':teampagemeta,
    }
    return render(request, 'mainapp/our-team.html',context)

def our_history(request):
    historypagesubtitle=Historypagesubtitle.objects.first()
    historysection=Historysection.objects.all()
    context = {
        'historypagesubtitle': historypagesubtitle,
        'historysection': historysection,
    }
    return render(request, 'mainapp/our-history.html',context)

def faq(request):
    faqpagesubtitle = Faqpagesubtitle.objects.first()
    faqpage = Faqpage.objects.all()
    faqpagemeta = Faqpagemeta.objects.first()
    context = {
        'faqpagesubtitle': faqpagesubtitle,
        'faqpage': faqpage,
        'meta': faqpagemeta,
    }
    return render(request, 'mainapp/faq.html',context)

def services_page(request):
    servicepagesubtitle = Servicepagesubtitle.objects.first()
    servicesection=Servicesection.objects.all()
    serviceskill = Serviceskill.objects.all()
    servicepagemeta = Servicepagemeta.objects.first()
    context = {
        'servicepagesubtitle':servicepagesubtitle,
        'servicesection': servicesection,
        'serviceskill': serviceskill,
        'meta': servicepagemeta,
    }
    return render(request, 'mainapp/services-page.html',context)

def contact_us(request):
    contactpagesubtitle = Contactpagesubtitle.objects.first()
    addresslocation = Addresslocation.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST.get('message', True)

        contact=Contact(name=name, email=email, message=message)
        contact.save()
    #     messages.success(request, 'You Order has been Successfully Submitted')

    context = {
        'contactpagesubtitle':contactpagesubtitle,
        'addresslocation':addresslocation,
    }

    return render(request, 'mainapp/contact-us.html',context)

def pricing_plans(request):
    pricingpagesubtitle = Pricingpagesubtitle.objects.first()
    pricingcard = Pricingcard.objects.all()
    pricingattibute = Pricingattibute.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        url=request.POST['url']
        address=request.POST.get('address', False);
        p_type=request.POST.get('p_type', False);
        
        subscribe=Pricingsubscribe(name=name, email=email, url=url, address=address, package_type=p_type)
        subscribe.save()
    
    # for i in pricingcard:
    #     for j in pricingattibute:
    #         if i==j.catagory:
    #             print(j.attibute)
    #     print()

    context = {
        'pricingpagesubtitle':pricingpagesubtitle,
        'pricingcard':pricingcard,
        'pricingattibute':pricingattibute,
    }
    return render(request, 'mainapp/pricing-plans.html',context)


def privacy_policy(request):
    privacypolicypagesubtitle = Privacypolicypagesubtitle.objects.first()
    privacypolicybody = Privacypolicybody.objects.first()
    context = {
        'privacypolicypagesubtitle':privacypolicypagesubtitle,
        'privacypolicybody':privacypolicybody,
    }
    return render(request, 'mainapp/privacy-policy.html',context)



