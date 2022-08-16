from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# 관리자 폼 커스터마이징(8/16)
class QuestionAdmin(admin.ModelAdmin):
     fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)