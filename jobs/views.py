from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from jobs.models import Job
from jobs.models import Cities, JobTypes


def joblist(request):
    # 按类别排序
    job_list = Job.objects.order_by('job_type')
    # 加载模板
    template = loader.get_template('joblist.html')
    # 上下文，是一个map
    context = {'job_list': job_list}

    for job in job_list:
        # 需要展示的两个字段，为枚举类型，需要转换为字符串
        job.job_city = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)  # pk 主键
        job.job_city = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exsit")

    return render(request, 'job.html', {'job': job})
