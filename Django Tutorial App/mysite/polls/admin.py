from django.contrib import admin
# Register your models here.
from .models import Question,Choice

#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date','question_text']
	fieldsets = [
		('Questions Published', {'fields': ['question_text']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text','pub_date','was_pub_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)