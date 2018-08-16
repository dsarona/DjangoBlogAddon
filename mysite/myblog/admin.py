#from django.contrib import admin

from django.contrib import admin # <- this is already there.
from myblog.models import Post
from myblog.models import Category

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')

class CategoryInline(admin.TabularInline):
    model = Post.categories.through

class PostAdmin(admin.ModelAdmin):
    fields=('title', 'text', 'author')
    inlines = [CategoryInline,]

admin.site.register(Post, PostAdmin)
# and a new admin registration
admin.site.register(Category, CategoryAdmin)
