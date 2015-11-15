from django.conf.urls import url, include
from django.contrib import admin

from base.views import UserCreateView

urlpatterns = [
    # ...
    url(r'^$', UserCreateView.as_view(), name='user_create'),
    url(r'^admin/', include(admin.site.urls)),
]
