from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Section
from .models import Item

class SectionListView(ListView):
    model = Section
    template_name = "{{ app_name }}/section-list.html"
    paginate_by = '10'

    def get_queryset(self, **kwargs):
        qs = super(SectionListView, self).get_queryset(**kwargs)
        qs = qs.prefetch_related('items')
        return qs

class ItemListView(ListView):
    """View of list of items"""
    model = Item
    template_name = "{{ app_name }}/item-list.html"
    paginate_by = '10'

    def get(self, request, *args, **kwargs):
        self.section_id = kwargs['section_id']
        res = super(ItemListView, self).get(request, *args, **kwargs)
        return res

    def get_queryset(self, **kwargs):
        qs = super(ItemListView, self).get_queryset(**kwargs)
        return qs.filter(section_id=self.section_id).select_related()


class ItemDetailView(DetailView):
    """View of list of items"""
    model = Item
    template_name = "{{ app_name }}/item-detail.html"
