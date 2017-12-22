from django.contrib import admin
from .models import Category, Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "user", "created")
    list_filter = ["created"]
    search_fields = ["title", "date"]
    ordering = ["id"]


admin.site.register(Category)
admin.site.register(Ticket, TicketAdmin)
