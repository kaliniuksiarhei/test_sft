from django.http import HttpResponse

from .models import Application


def get_unique_manufacturers(request, id):
    res = Application.objects.filter(contract=id).values_list('products__manufacturer_id').distinct()
    return HttpResponse(', '.join(map(str, [row[0] for row in res])))
