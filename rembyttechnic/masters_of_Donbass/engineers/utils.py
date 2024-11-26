from .models import Engineer
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_engineers(request, rep, results):

    page = request.GET.get('page')
    # results = 6
    paginator = Paginator(rep, results)

    try:
        rep = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        rep = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        rep = paginator.page(page)

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    custom_range = range(left_index, right_index)

    return custom_range, rep


def search_engineers(request):
    search_query = ''

    if request.GET.get('search_query'):  # получаем данные по имени name="search_query"стр16index.html
        search_query = request.GET.get('search_query')

    engi = Engineer.objects.filter(Q(name__icontains=search_query) |
                                   Q(i_info__icontains=search_query) |
                                   Q(all_info__icontains=search_query)
                                   )
    # i-регистронезависимый поиск contains-что в имени будет содержаться

    return engi, search_query
