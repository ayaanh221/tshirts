{"changed":true,"filter":false,"title":"urls.py","tooltip":"/reviews/urls.py","value":"from django.conf.urls import url\nfrom . import views\n\nurlpatterns = [\n    # ex: /\n    url(r'^$', views.review_list, name='review_list'),\n    # ex: /review/5/\n    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),\n    # ex: /tshirts/\n    url(r'^product$', product.product_list, name='products_list'),\n    # ex: /tshirts/5/\n    url(r'^product/(?P<wine_id>[0-9]+)/$', views.tshirts_detail, name='tshirts_detail'),\n]","undoManager":{"mark":-2,"position":26,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["from django.conf.urls import url","from . import views","","urlpatterns = [","    # ex: /","    url(r'^$', views.review_list, name='review_list'),","    # ex: /review/5/","    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),","    # ex: /wine/","    url(r'^wine$', views.wine_list, name='wine_list'),","    # ex: /wine/5/","    url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),","]"],"id":1}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":24},"action":"remove","lines":["views"],"id":2},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["t"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["s"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["h"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["i"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["r"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["t"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":27},"end":{"row":9,"column":31},"action":"remove","lines":["wine"],"id":3},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["t"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["s"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["h"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["i"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["r"]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["s"],"id":4}],[{"start":{"row":9,"column":12},"end":{"row":9,"column":15},"action":"remove","lines":["ine"],"id":5},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["w"]}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["t"],"id":6},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["s"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["h"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["i"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["r"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["s"],"id":7}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":15},"action":"remove","lines":["ine"],"id":8},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["w"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["t"],"id":9},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["s"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["h"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["i"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["r"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["t"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":15},"action":"remove","lines":["ine"],"id":10},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["w"]}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["t"],"id":11},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["s"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["g"],"id":12}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["h"],"id":13},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["i"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["r"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["t"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":68},"end":{"row":11,"column":72},"action":"remove","lines":["wine"],"id":14},{"start":{"row":11,"column":68},"end":{"row":11,"column":69},"action":"insert","lines":["t"]},{"start":{"row":11,"column":69},"end":{"row":11,"column":70},"action":"insert","lines":["s"]},{"start":{"row":11,"column":70},"end":{"row":11,"column":71},"action":"insert","lines":["h"]}],[{"start":{"row":11,"column":68},"end":{"row":11,"column":71},"action":"remove","lines":["tsh"],"id":15},{"start":{"row":11,"column":68},"end":{"row":11,"column":75},"action":"insert","lines":["tshirts"]}],[{"start":{"row":9,"column":50},"end":{"row":9,"column":54},"action":"remove","lines":["wine"],"id":16},{"start":{"row":9,"column":50},"end":{"row":9,"column":51},"action":"insert","lines":["t"]},{"start":{"row":9,"column":51},"end":{"row":9,"column":52},"action":"insert","lines":["s"]},{"start":{"row":9,"column":52},"end":{"row":9,"column":53},"action":"insert","lines":["h"]},{"start":{"row":9,"column":53},"end":{"row":9,"column":54},"action":"insert","lines":["i"]},{"start":{"row":9,"column":54},"end":{"row":9,"column":55},"action":"insert","lines":["r"]},{"start":{"row":9,"column":55},"end":{"row":9,"column":56},"action":"insert","lines":["t"]},{"start":{"row":9,"column":56},"end":{"row":9,"column":57},"action":"insert","lines":["s"]}],[{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"remove","lines":["e"],"id":17},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"remove","lines":["n"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"remove","lines":["i"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"remove","lines":["w"]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["t"],"id":18},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["s"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["h"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["i"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["r"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["t"]},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":52},"end":{"row":11,"column":53},"action":"remove","lines":["e"],"id":19},{"start":{"row":11,"column":51},"end":{"row":11,"column":52},"action":"remove","lines":["n"]},{"start":{"row":11,"column":50},"end":{"row":11,"column":51},"action":"remove","lines":["i"]},{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"remove","lines":["w"]}],[{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"insert","lines":["t"],"id":20},{"start":{"row":11,"column":50},"end":{"row":11,"column":51},"action":"insert","lines":["s"]},{"start":{"row":11,"column":51},"end":{"row":11,"column":52},"action":"insert","lines":["h"]},{"start":{"row":11,"column":52},"end":{"row":11,"column":53},"action":"insert","lines":["i"]},{"start":{"row":11,"column":53},"end":{"row":11,"column":54},"action":"insert","lines":["r"]},{"start":{"row":11,"column":54},"end":{"row":11,"column":55},"action":"insert","lines":["t"]},{"start":{"row":11,"column":55},"end":{"row":11,"column":56},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["from django.conf.urls import url","from . import views","","urlpatterns = [","    # ex: /","    url(r'^$', views.review_list, name='review_list'),","    # ex: /review/5/","    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),","    # ex: /tshirts/","    url(r'^tshirts$', tshirts.tshirts_list, name='tshirts_list'),","    # ex: /tshirts/5/","    url(r'^tshirts/(?P<wine_id>[0-9]+)/$', views.tshirts_detail, name='tshirts_detail'),","]"],"id":21}],[{"start":{"row":0,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["from django.conf.urls import url","from . import views","","urlpatterns = [","    # ex: /","    url(r'^$', views.review_list, name='review_list'),","    # ex: /review/5/","    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),","    # ex: /tshirts/","    url(r'^tshirts$', tshirts.tshirts_list, name='tshirts_list'),","    # ex: /tshirts/5/","    url(r'^tshirts/(?P<wine_id>[0-9]+)/$', views.tshirts_detail, name='tshirts_detail'),","]"],"id":22}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":18},"action":"remove","lines":["tshirts"],"id":23},{"start":{"row":11,"column":11},"end":{"row":11,"column":18},"action":"insert","lines":["product"]}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":18},"action":"remove","lines":["tshirts"],"id":24},{"start":{"row":9,"column":11},"end":{"row":9,"column":18},"action":"insert","lines":["product"]}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":29},"action":"remove","lines":["tshirts"],"id":25},{"start":{"row":9,"column":22},"end":{"row":9,"column":29},"action":"insert","lines":["product"]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":37},"action":"remove","lines":["tshirts"],"id":26},{"start":{"row":9,"column":30},"end":{"row":9,"column":37},"action":"insert","lines":["product"]}],[{"start":{"row":9,"column":50},"end":{"row":9,"column":56},"action":"remove","lines":["tshirt"],"id":27},{"start":{"row":9,"column":50},"end":{"row":9,"column":57},"action":"insert","lines":["product"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":14},"end":{"row":1,"column":19},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1596884423862}