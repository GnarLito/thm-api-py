import asyncio
import json
import sys
from asyncio.futures import Future
from urllib.parse import quote as _uriquote

import requests

import errors
import utils

# from .. import __version__
__version__ = "1"
GET = 'GET'
POST = 'POST'

def json_or_text(response):
    text = response.text
    try:
        if response.headers['content-type'].startswith('application/json'):
            return json.loads(text)
    except KeyError:
        # Thanks Cloudflare
        pass

    return text

class Route:
    BASE = "https://www.tryhackme.com"
    def __init__(self, method=GET, path='', **parameters):
        self.method = method
        self.path = path
        url = self.BASE + self.path
        
        if parameters:
            self.url = url.format(**{k: _uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})
        else:
            self.url = url
        
        self.bucket = f"{method} {path}"


class HTTPClient:
    def __init__(self, loop, connector=None):
        self.loop = loop
        self.__session = None
        self.connector = connector
        self.connect_sid = None
        
        self.user_agent = f'Tryhackme: (https://github.com/GnarLito/thm-api-py {__version__}) Python/{sys.version_info[0]}.{sys.version_info[1]} requests/{requests.__version__}'
    
    async def close(self):
        if self.__session:
            await self.__session.close()
    
    def login(self, session=None):
        self.connect_sid = session
        self.__session = requests.Session()
        cookie = requests.cookies.create_cookie('connect.sid', session, domain='tryhackme.com')
        self.__session.cookies.set_cookie(cookie)
        
    
    def request(self, route, **kwargs):
        endpoint = route.url
        method = route.method
        
        headers = {
            'User-Agent': self.user_agent
        }
        
        if 'json' in kwargs:
            headers['Content-Type'] = 'application/json'
            kwargs['data'] = utils.to_json(kwargs.pop('json'))

        data = []
        # TODO: retries
        try:
            with self.__session.request(method, endpoint, **kwargs) as r:
                
                r_data = json_or_text(r)
                
                # * valid return
                if 300 > r.status_code >= 200:

                    # $ if return url is login then no auth
                    if r.url.split('/')[-1] == "login":
                        raise errors.Unautherized(r, data)
                    
                    data.insert(0, r_data)
                    return data
                
                # $ no auth
                if r.status_code in {401, 403}:
                    raise errors.Unautherized(r, data)
                
                # $ endpoint not found
                if 404 == r.status_code:
                    raise errors.NotFound(r, data)
                
                # $ server side issue's
                if r.status_code in {500, 502}:
                    raise errors.ServerError(r, data)
        
        except Exception as e:           
            print("WebError", e)

    def get_test_req(self):
        return self.request(Route(GET, "/api/site-stats"))
    
class RouteList:
    def request(self, route, **kwargs): raise errors.NotImplemented()
    def get_server_time(self):  return self.request(Route(path="/api/server-time"))
    def get_site_stats(self):   return self.request(Route(path="/api/site-stats"))
    def get_server_time(self):  return self.request(Route(path="/api/leaderboards"))
    
class test_http:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.http = HTTPClient(loop=self.loop)
    
    def test(self):
        self.http.login()
        return self.http.get_test_req()

mytest = test_http()
print(mytest.test())
