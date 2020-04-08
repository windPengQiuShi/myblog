#article/urls.py

# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name='article_safe_delete'
    ),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    # 点赞 +1
    path('increase-likes/<int:id>/', views.IncreaseLikesView.as_view(), name='increase_likes'),

    # 列表类视图
    path('list-view/', views.ArticleListView.as_view(), name='list_view'),
    # 详情类视图
    path('detail-view/<int:pk>/', views.ArticleDetailView.as_view(), name='detail_view'),
    # 创建类视图
    path('create-view/', views.ArticleCreateView.as_view(), name='create_view'),
]