from django.contrib import admin
from womenProduct.models import womenCategoryTable, womenBrandTable, womenTagsTable, WomenProductTable, ImagesForWomenProduct

# Register your models here.
admin.site.register(womenCategoryTable)
admin.site.register(womenBrandTable)
admin.site.register(womenTagsTable)
admin.site.register(WomenProductTable)
admin.site.register(ImagesForWomenProduct)