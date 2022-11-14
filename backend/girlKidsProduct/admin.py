from django.contrib import admin
from girlKidsProduct.models import girlCategoryTable, girlBrandTable, girlTagsTable, GirlProductTable, ImagesForGirlProduct

# Register your models here.
admin.site.register(girlCategoryTable)
admin.site.register(girlBrandTable)
admin.site.register(girlTagsTable)
admin.site.register(GirlProductTable)
admin.site.register(ImagesForGirlProduct)
