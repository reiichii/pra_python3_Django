from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

# ビュー
# def hello(request):
#     # return HttpResponse('Hello World')
#
#     # テンプレートに渡す辞書
#     context = {'message': 'メッセージ'}
#     return TemplateResponse(request, 'item/message.html', context=context)

@login_required
def edit(request, item_id):

    item = get_object_or_404(Item, id=item_id)