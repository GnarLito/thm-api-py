from .question import Question
from .module import Module

# TODO: html elements removing
class RoomTask:
    def __init__(self, http, data):
        self.http = http
        self.questions = []
        
        self._from_data(data)
    
    def _from_data(self, data):
        self.title = data.get('taskTitle')
        self.description = data.get('taskDesc')
        self.type = data.get('taskType')
        self.number = data.get('taskNo')
        self.created = data.get('taskCreated')
        self.deadline = data.get('taskDeadline')
        self.uploadId = data.get('uploadId')
        self._sync(data)
    
    def _sync(self, data):
        self._questions = data.get('tasksInfo', []) if self.http.authenticated else data.get('questions', [])

    @property
    def questions(self):
        return [Question(http=self.http, data=question) for question in self._questions]


class PathTask:
    def __init__(self, http, data):
        self.http = http
        self._rooms = []
        self._from_data(data)
    
    def _from_data(self, data):
        self.id = data.get("_id")
        self.title = data.get("title")
        self._moduleURL = data.get("moduleURL")
        self.time = int(data.get("time"))
        self.overview = data.get("overview")
        self.outcomes = data.get("outcome")
        self.number = data.get("taskNo")
        self._rooms = data.get("rooms", [])
    
    @property
    def rooms(self):
        from .room import Room
        return [Room(http=self.http, data=self.http.get_room_details(room_code=room.get("code"))) for room in self._rooms]
    @property
    def module(self):
        return Module(http=self.http, moduleURL=self._moduleURL)
