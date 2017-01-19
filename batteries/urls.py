from django.conf.urls import url
from batteries.views import BatteryCreateView, BatteryUpdateView, BatteryDetailView, BatteryListView

urlpatterns = [
    url(r'^batteries/$', BatteryListView.as_view(), name='battery-list'),
    url(r'^batteries/add/$', BatteryCreateView.as_view(), name='battery-add'),
    url(r'^batteries/(?P<pk>[0-9]+)/update/$', BatteryUpdateView.as_view(), name='battery-update'),
    url(r'^batteries/(?P<pk>[0-9]+)/$', BatteryDetailView.as_view(), name='battery-detail'),
]