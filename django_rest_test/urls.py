from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view
from notice_board.views import notice_board_page, notice_api

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^rest-api/', include('rest_framework.urls')),
    re_path(r'^$', schema_view),

    # notice_board
    re_path(r'^notice_board/$', notice_board_page),

    # Rest
    re_path(r'^api/notice_board/$', notice_api.as_view()),
]
