from django import template
from kazakhapp.models import *

register = template.Library()
@register.simple_tag()
def get_city():
          return City.objects.all()


@register.inclusion_tag('index.html')
def get_artists(sort=None):
    if not sort:
        arts = Artist.objects.all()
    else:
        arts = Artist.objects.order_by(sort)
    return {'arts': arts}


