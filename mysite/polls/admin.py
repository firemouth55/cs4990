from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fields = ['question_text', 'pub_date']
	
	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
