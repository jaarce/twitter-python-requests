from django.views.generic.base import View
from django.http import HttpResponse
from django.core.cache import cache
import requests


class Feed(View):

    def get(self, request, *args, **kwargs):
        cached_feed = ''
        if not cache.get('feed'):
            headers = {'Authorization': 'OAuth oauth_consumer_key="ZxnF5b3sgoljsKyKTL4vI2Izm", oauth_nonce="9d69ef6a21f220ab3833095a562c2778", oauth_signature="fkUS1sQAQWUaJ58BQ%2BnnEN17mrc%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1431932850", oauth_token="77722070-M0J0diDqi8m0tWtrxIMDdHlPzEcTAo0zemLFw6lqA", oauth_version="1.0"'}
            payload = {'owner_screen_name':'itsmejohnandrew', 'slug':'interaksyon', 'count': 20}

            req = requests.get('https://api.twitter.com/1.1/lists/statuses.json', params=payload, headers=headers)

            cache.set('feed', req.content, 86400)
            cached_feed = req.content
        else:
            cached_feed = cache.get('feed')
        return HttpResponse(cached_feed, content_type='application/json')