from django.contrib import admin
from boyKidsProduct.models import boyCategoryTable, boyBrandTable, boyTagsTable, BoyProductTable, ImagesForBoyProduct

# Register your models here.
admin.site.register(boyCategoryTable)
admin.site.register(boyBrandTable)
admin.site.register(boyTagsTable)
admin.site.register(BoyProductTable)
admin.site.register(ImagesForBoyProduct)
