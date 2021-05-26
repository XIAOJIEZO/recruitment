from django.contrib import admin
from jobs.models import Job


# Register your models here.

class JobAdmin(admin.ModelAdmin):
    # ModelAdmin自带属性，隐藏字段（编辑页）
    exclude = ('creator', 'create_time', 'updata_time')
    # ModelAdmin自带属性，列表展示字段（列表页）
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'create_time', 'updata_time')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
