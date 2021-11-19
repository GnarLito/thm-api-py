from typing import Tuple
import errors
from urllib.parse import quote as _uriquote

GET='get'
POST='post'

class Route:
    # TODO: add post payload capabilities
    BASE = "https://www.tryhackme.com"
    def __init__(self, method=GET, path='', **parameters):
        self.method = method
        self.path = path
        url = self.BASE + self.path
        
        options = parameters.pop("options", None)
        if parameters:
            try:
                self.url = url.format(**{k: _uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})
            except Exception as e:
                raise errors.NotValidUrlParameters(e)
        else:
            self.url = url
        
        if options:
            if "?" not in self.url:
                self.url + "?" + "&".join([f"{i}={options[i]}" for i in options.keys() if options[i] != None])
            else:
                self.url + "&" + "&".join([f"{i}={options[i]}" for i in options.keys() if options[i] != None])
        
        self.bucket = f"{method} {path}"

# TODO: Redo ALL of this and only keeping the Routes in here... :|
# * url options not included (and defaults), post payload option missing
class RouteList:
    
    # * normal site calls
    
    def get_server_time(    self, **parameters): return Route(path="/api/server-time",    **parameters)
    def get_site_stats(     self, **parameters): return Route(path="/api/site-stats",     **parameters)
    def get_practise_rooms( self, **parameters): return Route(path="/api/practice-rooms", **parameters)
    def get_networks(       self, **parameters): return Route(path="/api/networks",       **parameters)
    def get_series(         self, **parameters): return Route(path="/api/series",         **parameters)
    def get_glossary_terms( self, **parameters): return Route(path="/glossary/all-terms", **parameters)
    
    # * Leaderboards
    
    def get_leaderboards(     self, **parameters): return Route(path="/api/leaderboards",      **parameters)
    def get_koth_leaderboards(self, **parameters): return Route(path="/api/leaderboards/koth", **parameters)
    
    # * account
    
    def get_subscription_cost(self, **parameters): return Route(path="/account/subscription/cost", **parameters)
    
    # * paths
    
    def get_path(           self, **parameters): return Route(path="/paths/single/{path_code}",  **parameters)
    def get_public_paths(   self, **parameters): return Route(path="/paths/public",              **parameters)
    def get_path_summary(   self, **parameters): return Route(path="/paths/summary",             **parameters)
    def get_modules_summary(self, **parameters): return Route(path="/modules/summary",           **parameters)
    
    # * games
    
    def get_machine_pool(   self, **parameters):  return Route(path="/games/koth/get/machine-pool",           **parameters)
    def get_game_detail(    self, **parameters):  return Route(path="/games/koth/data/{game_code}",           **parameters)
    def get_recent_games(   self, **parameters):  return Route(path="/games/koth/recent/games",               **parameters)
    def get_user_games(     self, **parameters):  return Route(path="/games/koth/user/games",                 **parameters)
    def get_game_tickets_won(self,**parameters):  return Route(path="/games/tickets/won?username={username}", **parameters)
    def post_join_koth(     self, **parameters):  return Route(method=POST, path="/games/koth/new",           **parameters) 
    def post_new_koth(      self, **parameters):  return Route(method=POST, path="/games/koth/join-public",   **parameters) # ? might change for premium
    
    # * VPN
    
    def get_available_vpns(self, **parameters): return Route(path="/vpn/get-available-vpns", **parameters)
    def get_vpn_info(      self, **parameters): return Route(path="/vpn/my-data",            **parameters)
    
    # * VM
    
    def get_machine_running(    self, **parameters): return Route(path="/api/vm/running",                **parameters)
    def post_renew_machine(     self, **parameters): return Route(method=POST, path="/api/vm/renew",     **parameters)
    def post_terminate_machine( self, **parameters): return Route(method=POST, path="/api/vm/terminate", **parameters)
    
    # * user -badge
    
    def get_own_badges( self, **parameters): return Route(path="/api/badges/mine",           **parameters)
    def get_user_badges(self, **parameters): return Route(path="/api/badges/get/{username}", **parameters)
    def get_all_badges( self, **parameters): return Route(path="/api/badges/get",            **parameters)
    
    # * user -team
    
    def get_team_info(self, **parameters): return Route(path="/api/team/is-member", **parameters)
    
    # * user -notifications
    
    def get_unseen_notifications(self, **parameters): return Route(path="/api/notifications/has-unseen", **parameters)
    def get_all_notifications(   self, **parameters): return Route(path="/api/notifications/get",        **parameters)
    
    # * user -messages
    
    def get_unseen_messages(   self, **parameters): return Route(path="/api/message/has-unseen",    **parameters)
    def get_all_group_messages(self, **parameters): return Route(path="/api/message/group/get-all", **parameters)
    
    # * user -room
    
    def get_user_completed_rooms_count( self, **parameters): return Route(path="/api/no-completed-rooms-public/{username}",    **parameters)
    def get_user_completed_rooms(       self, **parameters): return Route(path="/api/all-completed-rooms?username={username}", **parameters)
    def get_user_created_rooms(         self, **parameters): return Route(path="/api/created-rooms/{username}",                **parameters)
    
    # * user
    
    def get_user_rank(   self, **parameters): return Route(path="/api/user/rank/{username}",                     **parameters)
    def get_user_activty(self, **parameters): return Route(path="/api/user/activity-events?username={username}", **parameters)
    def get_all_friends( self, **parameters): return Route(path="/api/friend/all",                               **parameters)
    def get_discord_user(self, **parameters): return Route(path="/api/discord/user/{username}",                  **parameters) # ? rename to user profile
    def get_user_exist(  self, **parameters): return Route(path="/api/user/exist/{username}",                    **parameters)
    def search_user(     self, **parameters): return Route(path="/api/similar-users/{username}",                 **parameters)
    
    # * room
    
    def get_new_rooms(           self, **parameters): return Route(path="/api/new-rooms",                        **parameters)
    def get_recommended_rooms(   self, **parameters): return Route(path="/recommend/last-room?type=json",        **parameters)
    def get_questions_answered(  self, **parameters): return Route(path="/api/questions-answered",               **parameters)
    def get_joined_rooms(        self, **parameters): return Route(path="/api/my-rooms",                         **parameters)
    def get_room_percetages(     self, **parameters): return Route(method=POST, path="/api/room-percentages",    **parameters) # ? is a post but it gets stuff
    def get_room_scoreboard(     self, **parameters): return Route(path="/api/room/scoreboard?code={room_code}", **parameters)
    def get_room_votes(          self, **parameters): return Route(path="/api/room/votes?code={room_code}",      **parameters)
    def get_room_details(        self, **parameters): return Route(path="/api/room/details?codes={room_code}",   **parameters) # ? list posibility
    def get_room_tasks(          self, **parameters): return Route(path="/api/room/tasks/{room_code}",           **parameters)
    def post_room_answer(        self, **parameters): return Route(method=POST, path="/api/{room_code}/answer",  **parameters)
    def post_deploy_machine(     self, **parameters): return Route(method=POST, path="/material/deploy",         **parameters)
    def post_reset_room_progress(self, **parameters): return Route(method=POST, path="/api/reset-progress",      **parameters)
    def post_leave_room(         self, **parameters): return Route(method=POST, path="/api/room/leave",          **parameters)


class RequestList(RouteList):
    def request(self, route, **kwargs): raise errors.NotImplemented()
    
    # * normal site calls
    
    def get_server_time(self):
        return self.request(super.get_server_time())
    def get_site_stats(self):
        return self.request(super.get_site_stats())
    def get_practise_rooms(self): 
        return self.request(super.get_practise_rooms())
    def get_networks(self): 
        return self.request(super.get_networks())
    def get_series(self): 
        return self.request(super.get_series())
    def get_glossary_terms(self): 
        return self.request(super.get_glossary_terms())
    
    # * Leaderboards
    
    def get_leaderboards(self, country=None, type=None):
        return self.request(super.get_leaderboards(country=country, type=type))
    def get_koth_leaderboards(self, country=None, type=None):
        return self.request(super.get_koth_leaderboards(country=country, type=type))
    
    # * account
    
    def get_subscription_cost(self): 
        return self.request(super.get_subscription_cost())
    
    # * paths
    
    def get_path(self, path_code):
        return self.request(super.get_path(path_code=path_code))
    def get_public_paths(   self):
        return self.request(super.get_public_paths())
    def get_path_summary(   self):
        return self.request(super.get_path_summary())
    def get_modules_summary(self):
        return self.request(super.get_modules_summary())
    
    # * games
    
    def get_machine_pool(self):
        return self.request(super.get_machine_pool())
    def get_game_detail(self, game_code):
        return self.request(super.get_game_detail(game_code=game_code))
    def get_recent_games(self):
        return self.request(super.get_recent_games())
    def get_user_games(self):
        return self.request(super.get_user_games())
    def get_game_tickets_won(self, username):
        return self.request(super.get_game_tickets_won(username=username))
    def post_join_koth(self):
        return self.request(super.post_join_koth())
    def post_new_koth(self):
        return self.request(super.post_new_koth())
    
    # * VPN
    
    def get_available_vpns(self, type : Tuple('machines', 'networks')):
        return self.request(super.get_available_vpns(options={"type": type}))
    def get_vpn_info(self):
        return self.request(super.get_vpn_info())
    
    # * VM

    def get_machine_running(self):
        return self.request(super.get_machine_running())
    def post_renew_machine(self, room_code):
        return self.request(super.post_renew_machine(), json={"code": room_code, "_csrf": ""})
    def post_terminate_machine(self, room_code):
        return self.request(super.post_terminate_machine(), json={"code": room_code, "_csrf": ""})
    
    # * user -badge
    
    def get_own_badges(self):
        return self.request(super.get_own_badges())
    def get_user_badges(self, username):
        return self.request(super.get_user_badges(username=username))
    def get_all_badges(self):
        return self.request(super.get_all_badges())
    
    # * user -team
    
    def get_team_info(self): 
        return self.request(super.get_team_info())
    
    # * user -notifications
    
    def get_unseen_notifications(self):
        return self.request(super.get_unseen_notifications())
    def get_all_notifications(self):
        return self.request(super.get_all_notifications())

    # * user -messages

    def get_unseen_messages(self):
        return self.request(super.get_unseen_messages())
    def get_all_group_messages(self):
        return self.request(super.get_all_group_messages())
    
    # * user -room

    def get_user_completed_rooms_count(self, username):
        return self.request(super.get_user_completed_rooms_count(username=username))
    def get_user_completed_rooms(self, username, limit=10, page=1):
        return self.request(super.get_user_completed_rooms(username=username, options={"limit": limit, "page": page}))
    def get_user_created_rooms(self, username, limit=10, page=1):
        return self.request(super.get_user_created_rooms(username=username, options={"limit": limit, "page": page}))

    # * user

    def get_user_rank(self, username):
        return self.request(super.get_user_rank(username=username))
    def get_user_activty(self, username):
        return self.request(super.get_user_activty(username=username))
    def get_all_friends(self):
        return self.request(super.get_all_friends())
    def get_discord_user(self, username):
        return self.request(super.get_discord_user(username=username))
    def get_user_exist(self, username):
        return self.request(super.get_user_exist(username=username))
    def search_user(self, username):
        return self.request(super.search_user(username=username))

    # * room

    def get_new_rooms(self):
        return self.request(super.get_new_rooms())
    def get_recommended_rooms(self):
        return self.request(super.get_recommended_rooms())
    def get_questions_answered(self):
        return self.request(super.get_questions_answered())
    def get_joined_rooms(self):
        return self.request(super.get_joined_rooms())
    def get_room_percetages(self, room_codes : tuple):
        return self.request(super.get_room_percetages(), json={"rooms": room_codes})
    def get_room_scoreboard(self, room_code):
        return self.request(super.get_room_scoreboard(room_code=room_code))
    def get_room_votes(self, room_code):
        return self.request(super.get_room_votes(room_code=room_code))
    def get_room_details(self, room_code):
        return self.request(super.get_room_details(room_code=room_code))
    def get_room_tasks(self, room_code):
        return self.request(super.get_room_tasks(room_code=room_code))
    def post_room_answer(self, room_code, taskNo, questionNo, answer):
        return self.request(super.post_room_answer(room_code=room_code), json={"_csrf": "", "taskNo": taskNo, "questionNo": questionNo, "answer": answer})
    def post_deploy_machine(self, room_code, uploadId): # ? csrf token
        return self.request(super.post_deploy_machine(), json={"roomCode": room_code, "id": uploadId, "_csrf": ""})
    def post_reset_room_progress(self, room_code): # ? csrf token
        return self.request(super.post_reset_room_progress(), json={"code": room_code, "_csrf": ""})
    def post_leave_room(self, room_code): # ? csrf token
        return self.request(super.post_leave_room(), json={"code": room_code, "_csrf": ""})
    