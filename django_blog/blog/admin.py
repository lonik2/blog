from django.contrib import admin
from blog.models import category, comment, post

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(category, CategoryAdmin)
admin.site.register(post, PostAdmin)
admin.site.register(comment, CommentAdmin)


