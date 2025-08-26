from django.contrib import admin
from . models import Category,Blogs,Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','Category_name','created_at','updated_at')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','author','blog_image','status','is_featured','created_at','updated_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id','title','category__Category_name','status')

   
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comment)


