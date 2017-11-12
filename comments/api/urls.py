from django.conf.urls import url
from django.contrib import admin


from .views import (
    CommentListAPIView,
    CommentDetailView

    )

urlpatterns = [
    url(r'^(?P<id>\d+)/$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', CommentDetailView.as_view(), name='thread'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
