from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^iphone/$', views.iphone, name='iphone'),
    url(r'^htc/$', views.htc, name='htc'),
    url(r'^blackberry/$', views.blackberry, name='blackberry'),
    url(r'^samsung/$', views.samsung, name='samsung'),
    url(r'^sony/$', views.sony, name='sony'),
    url(r'^sony/xperia/', views.xperia, name='xperia'),
    url(r'^about/$', views.about, name='about'),
]

urlpatterns += [
    url(r'^login/$', views.login_page, name='login'),
]

urlpatterns += [
    url(r'^user/login/$', views.login),
    url(r'^user/logout/$', views.logout),
]
