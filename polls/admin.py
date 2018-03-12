from django.contrib import admin

# Import models
from . import models

admin.site.site_header = 'Polling App'
admin.site.site_title = 'Polling App'


# Register Choice Model
class ChoiceInline(admin.TabularInline):
    # list_display = ('choice_text', 'votes', 'question', 'id', )
    model = models.Choice
    extra = 3


# Register Question Model
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'published_recently', 'id', )
    inlines = [ChoiceInline]
    search_fields = ['question_text', ]

