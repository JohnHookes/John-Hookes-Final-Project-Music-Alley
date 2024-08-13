from django.contrib import admin
from .models import Gigs
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Gigs)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description',]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

