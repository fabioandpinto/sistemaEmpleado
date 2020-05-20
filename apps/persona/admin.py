from django.contrib import admin
from .models import Empleado, Habilidades


# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'department',
        'first_name',
        'last_name',
        'position',
        'full_name',
    )

    # funcion para armar el full name
    def full_name(self, obj):
        fullname = obj.first_name + ' ' + obj.last_name
        return fullname

    search_fields = (
        'last_name',
        'first_name',
    )
    list_filter = ('position',)


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
