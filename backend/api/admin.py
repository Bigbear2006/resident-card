from django.contrib import admin

from . import models

admin.site.register(models.Category)
admin.site.register(models.Event)
admin.site.register(models.CategoryEvent)
admin.site.register(models.Ticket)
admin.site.register(models.Card)
admin.site.register(models.Hospital)
admin.site.register(models.Bank)
