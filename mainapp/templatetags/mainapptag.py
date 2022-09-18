from django import template
from mainapp.models import *

# from django.template.loader import get_template

register = template.Library()

# @register.simple_tag
# def footersection(request):
#     return Footersection.objects.first()
# register.filter('footersection',footersection)

# @register.simple_tag(takes_context=True)
# def footer_section(context):
#     context = {}
#     try:
#         context['footeritem'] = Footersection.objects.first()
#         print('yes')
#     except:
#         context['footeritem'] = False
#     return context


# def show_users_table():
#     users = Footersection.objects.first()
#     return {'users': users}

# users_template = get_template('includes/footer.html')
# register.inclusion_tag(users_template)(show_users_table)

# render(self, context):

# @register.simple_tag(takes_context=True)
# def get_contact_us_section_text(context):
#     context = {}
#     try:
#         context['contact_us_section_text'] = Contactussection.objects.first()
#         print('yes')
#         print(type(context['contact_us_section_text']))
#     except:
#         context['contact_us_section_text'] = False
#     return context

# @register.filter(name='get_contact_us_section_text')

# def contact_us_section_text(request):
#     contactussection=Contactussection.objects.first()
#     return {'contactussection': contactussection}


# from django import template

# class CurrentTimeNode2(template.Node):
#     def __init__(self, format_string):
#         self.format_string = format_string
#     def render(self, context):
#         context = {}
#         try:
#             context['contact_us_section_text'] = Contactussection.objects.first()
#             print('yes')
#             print(type(context['contact_us_section_text']))
#         except:
#             context['contact_us_section_text'] = False
#         return context

