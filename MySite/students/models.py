from django.db import models
from datetime import datetime
# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    age = models.IntegerField(default=0, verbose_name="年龄")
    grade = models.CharField(max_length=10, verbose_name="班级")
    course = models.CharField(max_length=32, verbose_name="课程")
    enroll_date = models.DateField(default=datetime.now, verbose_name="注册时间")

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
