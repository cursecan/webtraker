from django.db import models

# Create your models here.


class PhisingWeb(models.Model):
    title = models.CharField(max_length=200, unique=True)
    name_parse = models.CharField(max_length=200)
    cat_parse = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/photo/')
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class TrackRecord(models.Model):
    web_load = models.ForeignKey(PhisingWeb, on_delete=models.CASCADE)
    ip_host = models.GenericIPAddressField()
    long_t = models.CharField(max_length=200, blank=True, null=True)
    lat_t = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_host


