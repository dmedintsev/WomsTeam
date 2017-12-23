from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "user", "date")
    list_filter = ["date"]
    search_fields = ["title", "date"]
    ordering = ["id"]


admin.site.register(Faq, FaqAdmin)
