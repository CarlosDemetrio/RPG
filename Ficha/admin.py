from django.contrib import admin

# Register your models here.
from .models import Ficha, Aptidao, Virtude, Up, Vantagem, Habilidade


class FichaAdmin(admin.ModelAdmin):
    list_display = ('nomePersonagem', 'tipo')
    search_fields = ['nomePersonagem']


admin.site.register(Ficha, FichaAdmin)
admin.site.register(Aptidao)
admin.site.register(Vantagem)
admin.site.register(Virtude)
admin.site.register(Up)
admin.site.register(Habilidade)