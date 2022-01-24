from django.contrib import admin


from .models import Testimonial,TopPlace
# Register your models here.

admin.site.register(Testimonial)
class TopPlaceAdmin(admin.ModelAdmin):
    list_display = ('id','place_name','place_city','place_state')
admin.site.register(TopPlace,TopPlaceAdmin)
