from datetime import datetime, timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200) # 질문 내용
    pub_date = models.DateTimeField("date published") # 질문 게시일

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문 외래키
    choice_text = models.CharField(max_length=200) # 선택 내용
    votes = models.IntegerField(default=0) # 투표 수

    def __str__(self):
        return self.choice_text
