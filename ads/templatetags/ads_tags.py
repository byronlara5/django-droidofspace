from ads.models import Ads
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.inclusion_tag('zinnia/tags/dummy.html')
def get_ads(template='zinnia/tags/index_ads.html'):
    #check to see if an entryphoto exists
     return {'template': template,
            'advs': Ads.objects.filter(index=True)[:4]}


@register.inclusion_tag('zinnia/tags/dummy.html')
def get_ads_article(template='zinnia/tags/article_ads.html'):
    #check to see if an entryphoto exists
     return {'template': template,
            'advs': Ads.objects.filter(article=True)[:3]}
