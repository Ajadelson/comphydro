from django.contrib import admin
from .models import Reduction,ReducedSerie,RollingMeanSerie

class ReductionAdmin(admin.ModelAdmin):
    model = Reduction
    list_display = ['type',]
    search_fields = ['type']
    save_on_top = True
class ReducedSerieAdmin(admin.ModelAdmin):
    model = ReducedSerie
    list_display = ['reduction',]
    search_fields = ['type']
    save_on_top = True
    
admin.site.register(Reduction,ReductionAdmin)
admin.site.register(ReducedSerie)