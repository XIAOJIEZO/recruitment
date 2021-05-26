from django.conf.urls import url
from jobs import views

urlpatterns = [
    url(r"^joblist/", views.joblist, name="joblist")
]
