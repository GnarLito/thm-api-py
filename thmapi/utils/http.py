import sys
import json

import requests

import errors
import utils
from routes import *
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

class HTTPClient(RouteList):
    def __init__(self, connector=None):
        self.__session = None
        self.connector = connector
        self.connect_sid = None
        
        self.user_agent = f'Tryhackme: (https://github.com/GnarLito/thm-api-py {__version__}) Python/{sys.version_info[0]}.{sys.version_info[1]} requests/{requests.__version__}'
    
    def close(self):
        if self.__session:
            self.__session.close()
    
    def login(self, session=None):
        self.connect_sid = session
        self.__session = requests.Session()
        cookie = requests.cookies.create_cookie('connect.sid', session, domain='tryhackme.com')
        self.__session.cookies.set_cookie(cookie)
        
    
    def request(self, route, **kwargs):
        endpoint = route.url
        method = route.method
        # settings = kwargs.pop('settings', None) ? do i need this
        
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
                        raise errors.Unauthorized(r, r_data)
                    
                    data.insert(0, r_data)
                    return data
                
                # $ no auth
                if r.status_code in {401, 403}:
                    raise errors.Unauthorized(r, r_data)
                
                # $ endpoint not found
                if 404 == r.status_code:
                    raise errors.NotFound(r, r_data)
                
                # $ server side issue's
                if r.status_code in {500, 502}:
                    raise errors.ServerError(r, r_data)
        
        except Exception as e:           
            print(e)

    def get_test_req(self):
        return self.request(Route(GET, "/api/site-stats"))
    

class test_http:
    def __init__(self, session=None):
        self.http = HTTPClient()
        self.http.login(session)
        

mytest = test_http()
print(mytest.http.get_subscription_cost())
