from django.contrib import admin
from menProduct.models import menCategoryTable, menBrandTable, menTagsTable, MenProductTable, ImagesForMenProduct

# Register your models here.
admin.site.register(menCategoryTable)
admin.site.register(menBrandTable)
admin.site.register(menTagsTable)
admin.site.register(MenProductTable)
admin.site.register(ImagesForMenProduct)
