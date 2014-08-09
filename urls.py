from django.conf.urls import patterns, include, url
from .views import ItemDetailView
from .views import ItemListView
from .views import SectionListView

urlpatterns = patterns('',
    url(r'section-list/$', SectionListView.as_view(), name='section-list'),
    url(r'item-list/(?P<section_id>\d+)/$', ItemListView.as_view(), name='item-list'),
    url(r'item-detail/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item-detail'),
)
