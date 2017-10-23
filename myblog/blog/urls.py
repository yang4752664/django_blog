from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^test/', views.Test, name="blog_test"),  # 测试的视图url规则
    url(r'^home/', views.home, name='blog_home'),  # 配置home url
    url(r'^post/(?P<id>\d+)/$', views.detail, name='blog_post'),  # 配置post url

]
