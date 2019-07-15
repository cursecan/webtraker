from django.contrib import admin

# Register your models here.

from .models import PhisingWeb, TrackRecord


@admin.register(PhisingWeb)
class PhisingWebAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_task_urls', 'timestamp']


    def get_task_urls(self, obj):
        return '/produk/i3/{}/{}/'.format(obj.cat_parse, obj.name_parse)

    get_task_urls.short_description = 'Url Palyload'


@admin.register(TrackRecord)
class TrackRecordAdmin(admin.ModelAdmin):
    list_display = ['ip_host', 'get_longlat', 'timestamp']

    def get_longlat(self, obj):
        return '{},{}'.format(obj.lat_t, obj.long_t)

    get_longlat.short_description = 'Longitude / Latitude'

    