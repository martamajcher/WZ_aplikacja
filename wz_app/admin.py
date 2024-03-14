from django.contrib import admin

from .models import Moje_wz


@admin.register(Moje_wz)
class Moje_wzAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}