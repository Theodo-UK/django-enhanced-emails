from django.contrib import admin
from django.utils.html import mark_safe

from .models import SentEmail


@admin.register(SentEmail)
class SentEmailAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("sent_at",)}),
        ("Email", {"fields": ("subject", ("to", "cc", "bcc"), "rendered_content")}),
        ("Raw data", {"classes": ("collapse",), "fields": ("raw_content",)}),
    )
    list_display = ("__str__", "to", "subject", "sent_at")
    list_filter = ("sent_at",)
    date_hierarchy = "sent_at"
    search_fields = ("subject", "to", "cc", "bcc")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def rendered_content(self, sent_email):
        return mark_safe(sent_email.content)

    rendered_content.short_description = "Content"

    def raw_content(self, sent_email):
        return sent_email.content

    raw_content.short_description = "Content"
