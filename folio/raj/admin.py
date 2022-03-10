from django.contrib import admin
from .models import Contact, Images, profile, projectimg, resume

# Register your models here.

admin.site.register(Contact)
admin.site.register(Images)
admin.site.register(projectimg)
admin.site.register(resume)
admin.site.register(profile)
