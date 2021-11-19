from .http import HTTP
from .state import State
from .network import Network

# TODO: build out Serie, Leaderboard, Hackivities (room search), HTML scrapper for username and CSRF token, error build out, state class build out, de HTML question object, message/notification class 
# ? maybe a writeup class bu maybe not

class Client:
    def __init__(self):
        self.http = HTTP()
        self._state = State(self.http)
        
        # TODO: Fetch username from TryHackMe via the HTML
        # self.user = self._state.store_client_user(username)
        
    def get_room(self, room_code):
        try:
            return self._state.store_room(room_code)
        except Exception as e:
            raise e # * pre definition for when exception overruling is needed
    
    def get_path(self, path_code):
        try:
            return self._state.store_path(path_code)
        except Exception as e:
            raise e # * pre definition for when exception overruling is needed

    def get_module(self, module_code):
        try:
            return self._state.store_module(module_code)
        except Exception as e:
            raise e # * pre definition for when exception overruling is needed
    
    def get_user(self, username):
        try:
            return self._state.store_user(username)
        except Exception as e:
            raise e # * pre definition for when exception overruling is needed
    
    # ! Not Implemented (build out state and this function aswell)
    def get_practice_rooms(self):
        rooms = self.http.get_practise_rooms()
        raise NotImplemented("Practice room API not yet worked out, if u want this feature please consider making a issue in the GitHub page.")

    # ! Not Implemented (network class / network API)
    # def get_network(self, network_code):
        # try:
        #    return Network(http=self.http, data=self.http.get_network(network_code=network_code))
        #     return self.http.search_room(room_code, page=page, order=order, difficulty=difficulty, type=type, free=free, limit=limit)
        # except Exception as e:
            # raise e # * pre definition for when exception overruling is needed
    
    # ! Not Implemented (hacktivities API) [hacktivities is bigger then one api call]
    # def search_room(self, room_code, page=1, order=None, difficulty=None, type=None, free=None, limit=None):
        # try:
        #     return self.http.search_room(room_code, page=page, order=order, difficulty=difficulty, type=type, free=free, limit=limit)
        # except Exception as e:
            # raise e # * pre definition for when exception overruling is needed
    
    def search_user(self, username):
        try:
            return self.http.search_user(username=username)
        except Exception as e:
            raise e # * pre definition for when exception overruling is needed
    
    @property
    def server_time(self):
        return self.http.get_server_time().get('datetime')
    @property
    def server_stats(self):
        return self.http.get_server_stats()
    @property
    def subscription_cost(self):
        return self.http.get_subscription_cost()
    @property
    def glossary(self):
        return self.http.get_glossary_terms()