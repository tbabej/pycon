from django.conf.urls import url, include
from django.contrib import admin

from base.views import SubmissionCreateView, download_submission

urlpatterns = [
    # ...
    url(r'^$', SubmissionCreateView.as_view(), name='submission_create'),
    url(r'download/(?P<submission_id>\d*)/$', download_submission, name='submission_download'),
    url(r'^admin/', include(admin.site.urls)),
]
