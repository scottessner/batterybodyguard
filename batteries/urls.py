from django.conf.urls import url
from batteries.views import BatteryCreate, BatteryUpdate, BatteryDetail, BatteryListView

urlpatterns = [
    url(r'^batteries/$', BatteryListView.as_view(), name='battery-list'),
    url(r'^batteries/add/$', BatteryCreate.as_view(), name='battery-add'),
    url(r'^batteries/(?P<pk>[0-9]+)/update/$', BatteryUpdate.as_view(), name='battery-update'),
    url(r'^batteries/(?P<pk>[0-9]+)/$', BatteryDetail.as_view(), name='battery-detail'),
]