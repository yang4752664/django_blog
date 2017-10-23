from django.contrib import admin
from blog.models import Article
# Register your models here.


# 用户管理类,仅显示博客标题和创建时间, 并在最下面进行注册
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


# 注册该模型类的用户管理,记得使用 python manage.py createsuperuser,登录后台管理
admin.site.register(Article, ArticleAdmin)
