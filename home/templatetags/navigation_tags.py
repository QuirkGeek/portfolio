from django import template
from wagtail.models import Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


@register.simple_tag(takes_context=True)
def get_live_index_titles(context):
    site_root = get_site_root(context)
    return site_root.get_children().live().in_menu().values_list('title', flat=True)