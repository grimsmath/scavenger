from django.contrib import admin
from .models import Sheet

# Register your models here.


@admin.register(Sheet)
class SheetAdmin(admin.ModelAdmin):
    list_display = ("id_number", "last_name", "first_name",
                    "sheet_num", "start_date", "end_date")
    search_fields = ("last_name", "first_name", "id_number")
