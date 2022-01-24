from django.contrib import admin
from places.models import placing,Comment
# Register your models here.

class placingAdmin(admin.ModelAdmin):
    list_display = ('id','place_name','place_city','place_state')
admin.site.register(placing,placingAdmin)
admin.site.register(Comment)