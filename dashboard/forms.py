from django import forms
from blogs.models import Category,Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


# blog post form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','category','blog_image','short_description','blog_body','status','is_featured')


# user form
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions')
    







