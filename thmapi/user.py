from .errors import NotImplemented

# TODO: add message/notification class 
class User:
    def __init__(self, http, username=None):
        self.http = http
        
        self.username = username
        self._completed_rooms = []
        
        if not self.http.get_user_exist(username=self.username).get('success', False):
            raise NotImplemented("Unknown user with username: "+ self.username)
        
        data = self._fetch()
        self._from_data(data)
    # TODO: fetch is a mess, needs fixing
    def _fetch(self):
        data = {}
        data['badges'] = self.http.get_user_badges(username=self.username)
        data['rank'] = self.http.get_discord_user(username=self.username)
        data['completed_rooms'] = self.http.get_user_completed_rooms(username=self.username)
        return data
    
    def _from_data(self, data):
        self.badges = data.get('badges')
        self.rank = data.get('rank').get('userRank')
        self.points = data.get('rank').get('points')
        self.subscribed = data.get('rank').get('subscribed')
        self._completed_rooms = data.get('completed_rooms')

    @property
    def completed_rooms(self):
        # * u gotta love circular imports
        from .room import Room
        return [Room(data=data) for data in self._completed_rooms]

