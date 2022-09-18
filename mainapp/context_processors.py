from mainapp.models import *
from django.shortcuts import render

def footer_section_text(request):
    footersection = Footersection.objects.first()
    return {'footersection': footersection}


def get_contact_us_section_text(request):
    contact_us_section_text = Contactussection.objects.first()
    return {'contact_us_section_text': contact_us_section_text}



# def newsletter(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         print(email)
#     return render(request, 'includes/footer.html')
