from django.shortcuts import render
from .models import News, FAQ, npa_documents, ts_orm
from loguru import logger

# Create your views here.
def index(request):
    #Выбираем для отрисовки последние 10 новостей
    news_list = News.objects.order_by('-news_date')[:10]
    if not news_list.exists():
        news_list = 'no data'
    faqs_list = FAQ.objects.all()[:10]
    npa_list = npa_documents.objects.all()[:15]
    ts_list = ts_orm.objects.all()[:5]
    context = {
        "news": news_list,
        "faqs": faqs_list,
        "npa": npa_list,
        "ts": ts_list,
        "rkn_color": 'red',
        "rkn_date": '01.01.1900',
        "rossv_color": 'red',
        "rossv_date": '01.01.1900',
        "hello": 'Для Вас мы собрали информацию из реестров Роскомандзора, Россвязи, сетрифицирующих органов. Также разработали и предлагаем воспользоваться шаблонами документов по тематике СОРМ',
    }
    #logger.debug(f"{context}")
    #data = serializers.serialize(format='json', queryset=data)
    return render(request, "main/index.html", context)


