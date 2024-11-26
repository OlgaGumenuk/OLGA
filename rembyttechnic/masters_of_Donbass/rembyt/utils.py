from .models import Repair
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_repair(request):
    search_query2 = ''

    if request.GET.get('search_query2'):  # получаем данные по имени name="search_query"
        search_query2 = request.GET.get('search_query2')

    rep = Repair.objects.distinct().filter(
        Q(type_of_repair__icontains=search_query2) |
        Q(description__icontains=search_query2)|
        Q(owner__name__icontains=search_query2)
    )

    return rep, search_query2


def paginate_repairs(request, rep, results):

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