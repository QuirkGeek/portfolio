from django.urls import path, reverse
from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.menu import MenuItem
from wagtail import hooks
from .views import index
from .models import HomePage


class BlogPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Home Pages"
    add_to_admin_menu = True
    model = HomePage

@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('calendar/', index, name='calendar'),
    ]

@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    return MenuItem('Calendar', reverse('calendar'), icon_name='date')



