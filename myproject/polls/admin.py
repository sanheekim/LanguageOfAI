from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# 관련된 객체 추가 (8/17)
# StackedInline보다 TabularInline이 조금 더 조밀한 테이블 기반 형식으로 표시
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
'''
# 관리자 폼 커스터마이징(8/16)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
'''

# 관리자 변경 목록(change list) 커스터마이징 (8/18)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)