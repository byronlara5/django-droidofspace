from invideos.models import Invideos
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.inclusion_tag('zinnia/tags/dummy.html')
def get_invideos(template='zinnia/tags/index_invideos.html'):
    #check to see if an entryphoto exists
     return {'template': template,
            'ivideos': Invideos.objects.filter(index=True)[:3]}


#@register.inclusion_tag('zinnia/tags/dummy.html')
#def get_ads_article(template='zinnia/tags/article_ads.html'):
#    #check to see if an entryphoto exists
#     return {'template': template,
#            'advs': Ads.objects.filter(article=True)[:3]}