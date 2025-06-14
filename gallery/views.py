from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from gallery.models import Collection, CollectionItem, SiteSettings


class CommonContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'site_settings': SiteSettings.get_site_settings(),
        })
        return context


class GalleryView(CommonContextMixin, ListView):
    """View for the gallery page displaying all collections."""
    model = Collection
    template_name = 'gallery/gallery.html'
    context_object_name = 'collections'


class CollectionView(DetailView):
    """View for displaying a specific collection and its items."""
    model = Collection
    template_name = 'gallery/collection.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()
        return context
