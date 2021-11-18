import sys
from urllib.parse import quote as _uriquote
import json
import aiohttp
import asyncio

import utils

# from .. import __version__
__version__ = "1"
GET = 'GET'
POST = 'POST'

async def json_or_text(response):
    text = await response.text(encoding='utf-8')
    try:
        if response.headers['content-type'] == 'application/json':
            return json.loads(text)
    except KeyError:
        # Thanks Cloudflare
        pass

    return text

class Route:
    BASE = "https://www.tryhackme.com"
    def __init__(self, method, path, **parameters):
        self.method = method
        self.path = path
        url = self.BASE + self.path
        
        if parameters:
            self.url = url.format(**{k: _uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})
        else:
            self.url = url


class HTTPClient:
    def __init__(self, loop, connector=None):
        self.loop = loop
        self.__session = None
        self.connector = connector
        self.connect_sid = None
        
        self.user_agent = f'Tryhackme: (https://github.com/GnarLito/thm-api-py {__version__}) Python/{sys.version_info[0]}.{sys.version_info[1]} aiohttp/{aiohttp.__version__}'
        
    def login(self, session=None):
        self.connect_sid = session
        self.__session = aiohttp.ClientSession(connector=self.connector, cookies={'connect.sid': self.connect_sid})
        
    async def request(self, route, **kwargs):
        endpoint = route.url
        method = route.method
        
        headers = {
            'User-Agent': self.user_agent
        }
        
        if 'json' in kwargs:
            headers['Content-Type'] = 'application/json'
            kwargs['data'] = utils.to_json(kwargs.pop('json'))

        data = []
        try:
            async with self.__session.request(method, endpoint, **kwargs) as r:
                
                r_data = await json_or_text(r)
                
                # * valid return
                if 300 > r.status >= 200:

                    # $ if return url is login then no auth
                    if r.url.raw_parts[-1] == "login":
                        raise
                    
                    data.insert(0, r_data)
                    return data
                
                # $ no auth
                if r.status in {401, 403}:
                    raise
                
                # $ endpoint not found
                if 404 == r.status:
                    raise
                
                # $ server side issue's
                if r.status in {500, 502}:
                    raise
        
        except Exception as e:
            print(e)

    async def get_test_req(self):
        return await self.request(Route(GET, "/glossary/all-terms"))
    
    
    
    
class test_http:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.http = HTTPClient(loop=self.loop)
        self.http.login()
        
    def run_await(self, func):
        loop = self.loop
        future = asyncio.ensure_future(func(), loop=loop)
        future.add_done_callback(lambda e: {loop.stop()})
        try: loop.run_forever()
        except: pass
        if not future.cancelled():
            try: return future.result()
            except: pass

    def test(self):
        async def test():
            return await self.http.get_test_req()
        return self.run_await(test)
    
mytest = test_http()
print(mytest.test())