from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from accounts.views import (login_view, register_view, logout_view)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^', include("posts.urls", namespace='posts')),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/posts/', include("posts.api.urls", namespace='posts-api')),
    url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),
     url(r'^api/comments/', include("comments.api.urls", namespace='comments-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)