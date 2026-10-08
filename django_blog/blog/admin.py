from django.contrib import admin
from blog.models import category, comment, post, postmedia

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostMediaInline(admin.TabularInline):
    model = postmedia
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostMediaInline]

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(category, CategoryAdmin)
admin.site.register(post, PostAdmin)
admin.site.register(comment, CommentAdmin)