from django.apps import AppConfig
import redis


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

red = redis.Redis(
    host='redis-14806.c284.us-east1-2.gce.cloud.redislabs.com',
    port=14806,
    password='yuGzbSllKh2tkllu4sTvNfbu0tXlIhbN',
)
