from django.template.response import TemplateResponse

# ビュー
def hello(request):
    # return HttpResponse('Hello World')

    # テンプレートに渡す辞書
    context = {'message': 'メッセージ'}
    return TemplateResponse(request, 'item/message.html', context=context)