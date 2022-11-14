from django.contrib import admin
from contact.models import contactTable, userMessage, footerAbout, footerCategories, footerUsefulLink

# Register your models here.
admin.site.register(contactTable)
admin.site.register(userMessage)
admin.site.register(footerAbout)
admin.site.register(footerCategories)
admin.site.register(footerUsefulLink)