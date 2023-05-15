from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dateCreation', 'categoryType')
    list_filter = ('author', 'dateCreation', 'postCategory')
    search_fields = ('title','postCategory__name', 'author__authorUser__username')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
