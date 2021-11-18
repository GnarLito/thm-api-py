from typing_extensions import ParamSpec
import aiohttp
from urllib.parse import quote as _uriquote


class request:
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
    def __init__(self, connector=None):
        self.__session = None
        self.connector = connector
        self.connect_sid = None
        
    def login(self, session):
        self.connect_sid = session
        self.session = aiohttp.ClientSession(connector=self.connector, cookies={'connect.sid': self.connect_sid})
        
    def request(self):
        pass
        