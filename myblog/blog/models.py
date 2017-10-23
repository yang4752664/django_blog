# coding=utf-8
from django.db import models
# from tinymce.models import HTMLField  # 导入富文本编辑器
from DjangoUeditor.models import UEditorField  # 导入DjangoUeditor
# Create your models here.


class ArticleManager(models.Manager):
    """博客文章模型管理器类"""
    pass


class Article(models.Model):
    """博客文章模型类"""
    title = models.CharField(max_length=100, verbose_name='博客标题')  # 博客标题
    # blank允许该字段为空,blank是表单验证范畴的,null是数据库范畴的
    blog_tag = models.CharField(max_length=50, verbose_name='博客标签', blank=True)  # 博客标签
    # editable：如果为假，admin模式下将不能改写。缺省为真
    # auto_now_time第一次被创建时自动设置为当前时间
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发布日期', editable=True)  # 博客发布日期
    # null允许字段为空,没有时默认返回空字符串
    # auto_time每次保存对象时,自动设置该字段为当前时间
    update_time = models.DateField(auto_now=True, null=True, verbose_name='更新时间')  # 博客更新时间
    '''
    # TextField 大文本字段
    # content = models.TextField(blank=True, null=True)  # 博客文章正文
    # 此处使用富文本编辑器,需要在当前应用下的admin注册该模型类
    # content = HTMLField(verbose_name='文章正文')  # 博客文章正文
    '''
    # 博客的正文使用DjangoUeditor的编辑器,在admin界面有更好的编辑
    content = UEditorField(height=300, width=1000, default='', blank=True, imagePath="uploads/blog.css/images/",
                           toolbars='besttome', filePath='uploads/blog.css/files/', verbose_name='文章正文')

    def __str__(self):  # 在管理者模式下显示博客的标题
        return self.title

    class Meta:  # 用meta类修改后 后台显示的模块名称
        # db_table 本模块在数据库中对应的表的名字
        db_table = 'blog_info'
        # verbose_name 是该对象的一个可读性更好的唯一名字
        verbose_name = '文章'
        # verbose_name_plural 对象名字的复数
        # 若未提供该选项, Django 会使用 verbose_name + "s"
        verbose_name_plural = verbose_name

    objects = ArticleManager()  # 实例化模型管理器





