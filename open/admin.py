from django.contrib import admin
from .models import Articles, Employee#,ForeignKeyModel


admin.site.register(Articles)
admin.site.register(Employee)
#admin.site.register(ForeignKeyModel)