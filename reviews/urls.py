from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /tshirts/
    url(r'^tshirts$', tshirts.tshirts_list, name='tshirts_list'),
    # ex: /tshirts/5/
    url(r'^tshirts/(?P<wine_id>[0-9]+)/$', views.tshirts_detail, name='tshirts_detail'),
]