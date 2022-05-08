from django import template

from mainPage.models import logInf, Regions

register = template.Library()# registarete our template tag

@register.simple_tag(name = 'get_regions_name')
def get_regions():
    return Regions.objects.all()

@register.inclusion_tag('mainPage/list_regions.html')
def show_regions():
    regions = Regions.objects.all()
    return {"reg": regions}
