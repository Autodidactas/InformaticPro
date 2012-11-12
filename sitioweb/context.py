from sitio.models import *
import datetime
#import GeoIP
import time

def globales(request):

	portada = Talleres.objects.filter(proximo=True)[:1]
	domingo = Videos.objects.filter(categoria=2,portada=True).order_by('-fecha')
	timestamp = get_timestamp()
	
	return {'portada': portada, 'domingo': domingo, 'timestamp':timestamp}

def domingo_taller(now):
    _4PM = datetime.time(hour=19)
    _JUE = 6  # Monday=0 for weekday()
    old_now = now
    now += datetime.timedelta((_JUE - now.weekday()) % 7)
    now = now.combine(now.date(), _4PM)
    if old_now >= now:
        now += datetime.timedelta(days=7)
    return now


def get_timestamp():
    now = datetime.datetime.now()
    sig_jueves = domingo_taller(now)
    return int(time.mktime(sig_jueves.timetuple()) * 1000)

#def get_pais(meta):
#    geo = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

    # por si el usuario esta detras de un proxy
#    if 'HTTP_X_FORWARDED_FOR' in meta and meta['HTTP_X_FORWARDED_FOR']:
#        ip = meta['HTTP_X_FORWARDED_FOR'].split(',')[0]
#    else:
#        ip = meta['REMOTE_ADDR']

#    country = geo.country_name_by_addr(ip)
#    if country is None:
#        country = ''

#    return country

