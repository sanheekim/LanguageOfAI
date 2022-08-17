from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# 관련된 객체 추가 (8/17)
# StackedInline보다 TabularInline이 조금 더 조밀한 테이블 기반 형식으로 표시
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 관리자 폼 커스터마이징(8/16)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)