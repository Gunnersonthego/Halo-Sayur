from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Certificate

# Register your models here.

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', )
    search_fields = ('first_name', 'last_name', )


admin.site.register(Certificate, CertificateAdmin)
