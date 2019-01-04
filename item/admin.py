from django.contrib import admin
# 関連モデルをインポート
from .models import Item, WishList

# 管理サイトへのモデルの登録
admin.site.register(Item)
admin.site.register(WishList)
