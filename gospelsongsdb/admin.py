from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy

from gospelsongsdb.models import Campi, Culto, Musica

# admin.site.site_title = ugettext_lazy('CEU Min. de Louvor')
# admin.site.site_header = ugettext_lazy('CEU Min. de Louvor')
# admin.site.index_title = ugettext_lazy('Administracao do CEU Min. de Louvor')

class CampiAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_filter=[]
    _fields=['name','address', 'capacity']
    list_display = _fields
    list_display_links = list_display
admin.site.register(Campi, CampiAdmin)

class MusicaAdmin(admin.ModelAdmin):
    search_fields=['name', 'tune', 'band','lyrics']
    list_filter=[]
    _fields=['name', 'tune', 'band','lyrics','link']
    list_display = _fields
    list_display_links = list_display
    ordering = ['name']
admin.site.register(Musica, MusicaAdmin)

class CultoAdmin(admin.ModelAdmin):
    filter_horizontal = ('musicas',)
#     formfield_overrides = {
#         models.ManyToManyField: {'widget': CheckboxSelectMultiple},
#     }  
    search_fields=['date']
    list_filter=[]
    _fields=['date', 'campi']
    list_display = _fields
    list_display_links = list_display
admin.site.register(Culto, CultoAdmin)