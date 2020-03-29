from django.contrib import admin

# 别忘了导入ArticlerPost
from .models import ArticlePost
from .models import ArticleColumn

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)