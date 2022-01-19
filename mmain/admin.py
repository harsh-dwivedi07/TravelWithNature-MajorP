from django.contrib import admin

from places.models import placing
from .models import Testimonial,TopPlace
# Register your models here.

admin.site.register(Testimonial)
admin.site.register(TopPlace)
admin.site.register(placing)