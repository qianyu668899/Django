from django.contrib import admin

# Register your models here.
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
	 ('Question', {'fields':['question'], 'classes':['collapse']}),
	 ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]

	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

admin.site.register(Poll, PollAdmin)
