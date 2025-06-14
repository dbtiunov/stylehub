from django.contrib import admin
from .models import SiteSettings, Collection, CollectionItem

class CollectionItemInline(admin.TabularInline):
    """Inline admin for CollectionItems within a Collection."""
    model = CollectionItem
    extra = 1

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Admin for SiteSettings model."""
    list_display = ('site_name', 'instagram_profile')

    def has_add_permission(self, request):
        """Prevent creating multiple site settings."""
        # Only allow adding if no settings exist yet
        return SiteSettings.objects.count() == 0

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Admin for Collection model."""
    list_display = ('title', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CollectionItemInline]
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

@admin.register(CollectionItem)
class CollectionItemAdmin(admin.ModelAdmin):
    """Admin for CollectionItem model."""
    list_display = ('title', 'collection', 'url', 'created_at')
    list_filter = ('collection', 'created_at')
    search_fields = ('title', 'url')
    autocomplete_fields = ('collection',)
