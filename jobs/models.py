from django.db import models
from django.contrib.auth.models import User

JobTypes = [
    (0, "技术类"),
    (1, "产品运营类"),
    (2, "内容类"),
]

Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳"),
]


# Create your models here.
class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=200, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name="工作地点")
    job_responsibilities = models.TextField(max_length=200, verbose_name="职位职责")
    job_requirements = models.TextField(max_length=200, blank=False, verbose_name="职位要求")
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="创建人")
    create_time = models.TimeField(verbose_name="创建时间")
    updata_time = models.TimeField(verbose_name="更新时间")
