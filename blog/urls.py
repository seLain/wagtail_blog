"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

app_name = 'blog' # register name

urlpatterns = [
    path('tag/<tag>/', views.tag_view, name="tag"),
    path('category/<category>/feed', views.LatestCategoryFeed(), name="category_feed"),
    path('category/<category>/', views.category_view, name="category"),
    path('author/<author>/', views.author_view, name="author"),
    re_path(r'(?P<blog_slug>[\w-]+)/rss.*/',
        views.LatestEntriesFeed(),
        name="latest_entries_feed"),
    re_path(r'(?P<blog_slug>[\w-]+)/atom.*/',
        views.LatestEntriesFeedAtom(),
        name="latest_entries_feed_atom"),
]
