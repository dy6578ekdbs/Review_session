from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # 생성 시의 시각 : date published

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #foreignkey는 다대일 관계, 두가지 위치 인수 필요 
    #CASCADE : 연관된 걸 삭제하는 놈
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    #__str__ 객체를 문자열로 표현한 것을 반환해주는 함수 


