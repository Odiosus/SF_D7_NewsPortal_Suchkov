# ✅создали файл самостоятельно и импортировали пути
from django.urls import path
# ✅импорт представлений
from .views import NewsList, NewsDetail, SearchView, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate
from .views import ArticleDelete

urlpatterns = [
    # path — путь.
    # путь ко всем новостям остаётся пустым
    # объявленное представление является классом — представляем этот класс в виде view
    # вызываем метод as_view.
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='one_news'),
    # регистрируем новое представление SearchView
    path('search/', SearchView.as_view(), name='search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]