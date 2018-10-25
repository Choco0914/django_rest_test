from django.db import models

"""
간단한 게시판 만들기

게시판은 다양한 포스트(Post) 단위로 구분되며,
하나의 포스팅에는 제목 / 내용 / 작성시간 등으로 구분된다.

즉 '제목' / '내용' / '작성 시간' 이 이 데이터의 기본이다.
"""
class Post(models.Model):
    """제목, 내용, 작성시간을 정의해준다."""
    title = models.CharField(max_length=256)
    contents = models.CharField(max_length=2048)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)
