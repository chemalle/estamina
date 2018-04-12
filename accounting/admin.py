from django.contrib import admin
from .models import Accounting
# Register your models here.



class AccountingAdmin(admin.ModelAdmin):
    list_display =["__str__","origem","destino","valorReais"]
    search_fields = ["valorReais","observacao"]
    list_filter = ["categoria","tipo"]
    list_editable = ["valorReais"]
    class Meta:
        model = Accounting

admin.site.register(Accounting, AccountingAdmin)
