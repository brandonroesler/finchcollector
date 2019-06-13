from django.contrib import admin
from .models import Bird, Feeding, Language, Photo

# Register your models here.
admin.site.register(Bird)
admin.site.register(Feeding)
admin.site.register(Language)
admin.site.register(Photo)
