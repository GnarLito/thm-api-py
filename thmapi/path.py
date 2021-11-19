from .user import User
from .task import PathTask
from .module import Module

class Path:
    def __init__(self, http, data):
        self.http = http
        
        self._badges = []
        self._careers = []
        self._modules = []
        self._tasks = []
        
        if data.get("username", None) is None:
            data = self._fetch(data)
        self._from_data(data)
    
    def _fetch(self, data):
        return self.http.get_path(path_code=data.get("code"))
    
    def _from_data(self, data):
        self.code = data.get("code")
        self.description = data.get("description")
        self.color = data.get("color")
        self.intro = data.get("intro")
        self.type = data.get("contentType")
        self.public = data.get("public", False)
        self.room_count = data.get("roomNo")
        self.summary = data.get("summary")
        self.careers = data.get("careers", [])
        self.difficulty = data.get("easy")
        self.time_to_complete = data.get("timeToComplete")
        self._modules = data.get("modules", [])
        self._badges = data.get("badges", [])
        self._tasks = data.get("tasks", [])
        
        self._sync(data)

    def _sync(self, data):
        self.user = User(http=self.http, username=data.get('username'))

    @property
    def tasks(self):
        return [PathTask(http=self.http, data=task) for task in self._tasks]
    @property
    def modules(self):
        return [Module(http=self.http, data=module.get('moduleURL')) for module in self._module]
    # TODO: badge class
    @property
    def badges(self):
        return [badge for badge in self._badges]
    @property
    def careers(self):
        return [career for career in self._careers]
