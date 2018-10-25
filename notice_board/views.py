from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from .models import Post

def notice_board_page(request):
    """기본 페이지를 정의하는 뷰"""
    post_list = Post.objects.all()

    return HttpResponse('Hello! ' + post_list[0].title)

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer 는 REST 로 데이터를 주고 받을 때, 모델을 어떻게 주고 받을 것인가를
    정의하기 위한 클래스 이다. 데이터 모델 그자체를 주고 받을 것이니, 기본적으로 모델
    전체를 자동으로 변환해주는 ModelSerializer에 힘을 빌렸다.
    """
    class Meta:
        """모델과 모델의 필드에 대한 정보를 여기다 정의해준다."""
        model = Post
        fields = ('title', 'contents', 'reg_date')

class notice_api(GenericAPIView, mixins.ListModelMixin):
    """
    ListModelMixin로 리스트를 자동으로 생성해주고로 구현하는 뷰
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        """
        REST Framework 에서는 request, *args, **kwargs를 반드시 포함해서 처리하게
        되어 있다. 기본적으로 온 요청에 대한 Pasing 작업을 하여 Request를 생성하고,
        그 외에 여러 데이터는 *args와 **kwargs에 포함하여 오는 형태이다.
        """
        return self.list(request, *args, **kwargs)
