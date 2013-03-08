from listem.models import Lists
from listem.models import Items 
from django.contrib import admin

class ItemsInline(admin.TabularInline):
	model = Items
	extra = 3

class ListsAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, 				 {'fields': ['title']}),
	('Date Information', {'fields': ['created'], 'classes': ['collapse']}),
	]
	inlines = [ItemsInline]
	list_display = ('title', 'created', 'was_added_recently')
	list_filter = ['created']
	search_fields = ['title']
	date_hierarchy ='created'

admin.site.register(Lists, ListsAdmin)