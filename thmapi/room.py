from .errors import NotImplemented
from .user import User
from .task import RoomTask

# ? writeups class

class Room:
    def __init__(self, http, room_code, data):
        self.http = http
        self.tasks = []
        self.writeups = []
        self.creators = []
        
        data = data.get(room_code, None)
        if data is None or not data.get('success', False):
            raise NotImplemented("failed to create room, no success value returned")
        
        self._from_data(data)
        
    def _from_data(self, data):
        self.name = data.get("roomCode")
        self.id = data.get("roomId")
        self.title = data.get("title")
        self.description = data.get("description")
        self.created = data.get("created")
        self.published = data.get("published")
        self.users = data.get("users")
        self.type = data.get("type")
        self.public = data.get("public")
        self.difficulty = data.get("difficulty")
        self.freeToUse = data.get("freeToUse")
        self.ctf = data.get("ctf")
        self.tags = data.get("tags")
        self.ipType = data.get("ipType")
        self.simpleRoom = data.get("simpleRoom")
        self.writeups = data.get("writeups")
        self.locked = data.get("locked")
        self.comingSoon = data.get("comingSoon")
        self.views = data.get("views")
        self.certificate = data.get("certificate")
        self.timeToComplete = data.get("timeToComplete")
        self.userCompleted = data.get("userCompleted")
        self._creators = data.get("creators")
    
    @property
    def question_count(self):
        count = 0
        for task in self.tasks:
            count += task.questions.__len__()
        return count
    @property
    def precentage(self):
        try: return self.http.get_room_percentages(room_codes=self.name)
        except: return {"roomCode": self.name, "correct": 0, "total":self.question_count, "prec": 0}
    @property
    def votes(self):
        return self.http.get_room_votes(room_code=self.name)
    @property
    def scoreboard(self):
        return self.http.get_room_scoreboard(room_code=self.name)
    @property
    def tasks(self):
        # TODO: is user is premium room tasks should be available or when not tasks are still available when session is not used
        if self.freeToUse:
            return [RoomTask(http=self.http, data=task) for task in self.http.get_room_tasks(room_code=self.name)]
        else: []
    @property
    def creators(self):
        return [User(http=self.http, username=user.get('username')) for user in self._creators]
    