from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound

from .models import Application, Manufacturer


def from_application(request, id):
    try:
        application = Application.objects.get(contract=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Application not found')

    manufacturers = Manufacturer.objects.filter(products__application=application.id).distinct()
    return HttpResponse(', '.join(map(str, [m.id for m in manufacturers])))


def one_query(request, id):
    manufacturers = Manufacturer.objects.filter(products__application__contract=id).distinct()
    return HttpResponse(', '.join(map(str, [m.id for m in manufacturers])))
