from .room import Room
from .errors import NotImplemented


class Module:
    def __init__(self, http, data=None, moduleURL=None):
        self.http = http
        
        if data is None:
            data = self._fetch(moduleURL)
        self._from_data(data)
    
    def _fetch(self, moduleURL):
        if moduleURL is None: raise NotImplemented("can't create module, module URL is None")
        return self.http.get_module(module_code=moduleURL)
        
    def _from_data(self, data):
        self.name = data.get('moduleURL').replace('-', ' ') # * the api leaves this http save
        self.code = data.get('moduleURL')
        self.id = data.get('id')
        self.description = data.get('description')
        self.summary = data.get('summary')
        self._rooms = data.get('rooms')
        self._prerequisites = data.get('prerequisites')
        self._nextSteps = data.get('nextSteps')

    @property
    def rooms(self):
        return [Room(http=self.http, data=room) for room in self._rooms]
    @property
    def prerequisites(self):
        return [Module(http=self.http, data=module) for module in self._prerequisites]
    @property
    def nextSteps(self):
        return [Module(http=self.http, data=module) for module in self._nextSteps]

