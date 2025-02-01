# from django.contrib import admin
# from .models import FAQ

# @admin.register(FAQ)
# class FAQAdmin(admin.ModelAdmin):
#     list_display = ("question", "question_hi", "question_bn")

from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)
