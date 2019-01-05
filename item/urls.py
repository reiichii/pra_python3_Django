from django.conf.urls import url

from . import views

# ルーティングの設定
urlpatterns = [
    #url(r'^hello/$', views.hello, name='hello'), # hello関数が呼ばれる

    # itemの一覧
    url(r'^$', views.index, name='item_index'),
    # 更新
    url(r'^(?P<item_id>[0-9]+)/edit/$', views.edit, name='item_edit'),
    # 削除
    url(r'^(?P<item_id>[0-9]+)/delete/$', views.delete, name='item_delete'),
    # ほしい物リストへの追加
    url(r'^(?P<item_id>[0-9]+)/add/wish_list/$', views.add_to_wish_list, name='item_add_wish_list'),
    # ほしい物リストへの削除
    url(r'^(?P<item_id>[0-9]+)/delete/wish_list/$', views.delete_from_wish_list, name='item_delete_wish_list'),
    # ほしい物リストの一覧
    url(r'^wish_list/$', views.wish_list_index, name='wish_list_index'),
]