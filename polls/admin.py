from django.contrib import admin

# Import models
from . import models

admin.site.site_header = 'Polling App'
admin.site.site_title = 'Polling App'


# Register Question Model
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'published_recently', )


# Register Choice Model
@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question', )