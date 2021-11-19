from typing import Tuple
import errors
from urllib.parse import quote as _uriquote
from cog import Cog
from convertors import (_county_types, _leaderboard_types, _vpn_types)

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

class RouteList:
    
    # * normal site calls
    
    def get_server_time(    **parameters): return Route(path="/api/server-time",    **parameters)
    def get_site_stats(     **parameters): return Route(path="/api/site-stats",     **parameters)
    def get_practise_rooms( **parameters): return Route(path="/api/practice-rooms", **parameters)
    def get_networks(       **parameters): return Route(path="/api/networks",       **parameters)
    def get_series(         **parameters): return Route(path="/api/series",         **parameters)
    def get_glossary_terms( **parameters): return Route(path="/glossary/all-terms", **parameters)
    
    # * Leaderboards
    
    def get_leaderboards(     **parameters): return Route(path="/api/leaderboards",      **parameters)
    def get_koth_leaderboards(**parameters): return Route(path="/api/leaderboards/koth", **parameters)
    
    # * account
    
    def get_subscription_cost(**parameters): return Route(path="/account/subscription/cost", **parameters)
    
    # * paths
    
    def get_path(           **parameters): return Route(path="/paths/single/{path_code}",  **parameters)
    def get_public_paths(   **parameters): return Route(path="/paths/public",              **parameters)
    def get_path_summary(   **parameters): return Route(path="/paths/summary",             **parameters)
    def get_modules_summary(**parameters): return Route(path="/modules/summary",           **parameters)
    
    # * games
    
    def get_machine_pool(    **parameters):  return Route(path="/games/koth/get/machine-pool",           **parameters)
    def get_game_detail(     **parameters):  return Route(path="/games/koth/data/{game_code}",           **parameters)
    def get_recent_games(    **parameters):  return Route(path="/games/koth/recent/games",               **parameters)
    def get_user_games(      **parameters):  return Route(path="/games/koth/user/games",                 **parameters)
    def get_game_tickets_won(**parameters):  return Route(path="/games/tickets/won?username={username}", **parameters)
    def post_join_koth(      **parameters):  return Route(method=POST, path="/games/koth/new",           **parameters) 
    def post_new_koth(       **parameters):  return Route(method=POST, path="/games/koth/join-public",   **parameters) # ? might change for premium
    
    # * VPN
    
    def get_available_vpns(**parameters): return Route(path="/vpn/get-available-vpns", **parameters)
    def get_vpn_info(      **parameters): return Route(path="/vpn/my-data",            **parameters)
    
    # * VM
    
    def get_machine_running(    **parameters): return Route(path="/api/vm/running",                **parameters)
    def post_renew_machine(     **parameters): return Route(method=POST, path="/api/vm/renew",     **parameters)
    def post_terminate_machine( **parameters): return Route(method=POST, path="/api/vm/terminate", **parameters)
    
    # * user -badge
    
    def get_own_badges( **parameters): return Route(path="/api/badges/mine",           **parameters)
    def get_user_badges(**parameters): return Route(path="/api/badges/get/{username}", **parameters)
    def get_all_badges( **parameters): return Route(path="/api/badges/get",            **parameters)
    
    # * user -team
    
    def get_team_info(**parameters): return Route(path="/api/team/is-member", **parameters)
    
    # * user -notifications
    
    def get_unseen_notifications(**parameters): return Route(path="/api/notifications/has-unseen", **parameters)
    def get_all_notifications(   **parameters): return Route(path="/api/notifications/get",        **parameters)
    
    # * user -messages
    
    def get_unseen_messages(   **parameters): return Route(path="/api/message/has-unseen",    **parameters)
    def get_all_group_messages(**parameters): return Route(path="/api/message/group/get-all", **parameters)
    
    # * user -room
    
    def get_user_completed_rooms_count( **parameters): return Route(path="/api/no-completed-rooms-public/{username}",    **parameters)
    def get_user_completed_rooms(       **parameters): return Route(path="/api/all-completed-rooms?username={username}", **parameters)
    def get_user_created_rooms(         **parameters): return Route(path="/api/created-rooms/{username}",                **parameters)
    
    # * user
    
    def get_user_rank(   **parameters): return Route(path="/api/user/rank/{username}",                     **parameters)
    def get_user_activty(**parameters): return Route(path="/api/user/activity-events?username={username}", **parameters)
    def get_all_friends( **parameters): return Route(path="/api/friend/all",                               **parameters)
    def get_discord_user(**parameters): return Route(path="/api/discord/user/{username}",                  **parameters) # ? rename to user profile
    def get_user_exist(  **parameters): return Route(path="/api/user/exist/{username}",                    **parameters)
    def search_user(     **parameters): return Route(path="/api/similar-users/{username}",                 **parameters)
    
    # * room
    
    def get_new_rooms(           **parameters): return Route(path="/api/new-rooms",                        **parameters)
    def get_recommended_rooms(   **parameters): return Route(path="/recommend/last-room?type=json",        **parameters)
    def get_questions_answered(  **parameters): return Route(path="/api/questions-answered",               **parameters)
    def get_joined_rooms(        **parameters): return Route(path="/api/my-rooms",                         **parameters)
    def get_room_percetages(     **parameters): return Route(method=POST, path="/api/room-percentages",    **parameters) # ? is a post but it gets stuff
    def get_room_scoreboard(     **parameters): return Route(path="/api/room/scoreboard?code={room_code}", **parameters)
    def get_room_votes(          **parameters): return Route(path="/api/room/votes?code={room_code}",      **parameters)
    def get_room_details(        **parameters): return Route(path="/api/room/details?codes={room_code}",   **parameters) # ? list posibility
    def get_room_tasks(          **parameters): return Route(path="/api/room/tasks/{room_code}",           **parameters)
    def post_room_answer(        **parameters): return Route(method=POST, path="/api/{room_code}/answer",  **parameters)
    def post_deploy_machine(     **parameters): return Route(method=POST, path="/material/deploy",         **parameters)
    def post_reset_room_progress(**parameters): return Route(method=POST, path="/api/reset-progress",      **parameters)
    def post_leave_room(         **parameters): return Route(method=POST, path="/api/room/leave",          **parameters)


class RequestList(RouteList, Cog):
    def request(self, route, **kwargs): raise errors.NotImplemented()
    
    # * normal site calls
    
    def get_server_time(self):
        return self.request(RouteList.get_server_time())
    def get_site_stats(self):
        return self.request(RouteList.get_site_stats())
    def get_practise_rooms(self): 
        return self.request(RouteList.get_practise_rooms())
    def get_networks(self): 
        return self.request(RouteList.get_networks())
    def get_series(self): 
        return self.request(RouteList.get_series())
    def get_glossary_terms(self): 
        return self.request(RouteList.get_glossary_terms())
    
    # * Leaderboards
    
    def get_leaderboards(self, country: _county_types=None, type:_leaderboard_types=None):
        return self.request(RouteList.get_leaderboards(country=country, type=type))
    def get_koth_leaderboards(self, country: _county_types=None, type:_leaderboard_types=None):
        return self.request(RouteList.get_koth_leaderboards(country=country, type=type))
    
    # * account
    
    def get_subscription_cost(self): 
        return self.request(RouteList.get_subscription_cost())
    
    # * paths
    
    def get_path(self, path_code):
        return self.request(RouteList.get_path(path_code=path_code))
    def get_public_paths(self):
        return self.request(RouteList.get_public_paths())
    def get_path_summary(self):
        return self.request(RouteList.get_path_summary())
    def get_modules_summary(self):
        return self.request(RouteList.get_modules_summary())
    
    # * games
    
    def get_machine_pool(self):
        return self.request(RouteList.get_machine_pool())
    def get_game_detail(self, game_code):
        return self.request(RouteList.get_game_detail(game_code=game_code))
    def get_recent_games(self):
        return self.request(RouteList.get_recent_games())
    def get_user_games(self):
        return self.request(RouteList.get_user_games())
    def get_game_tickets_won(self, username):
        return self.request(RouteList.get_game_tickets_won(username=username))
    def post_join_koth(self):
        return self.request(RouteList.post_join_koth())
    def post_new_koth(self):
        return self.request(RouteList.post_new_koth())
    
    # * VPN
    
    def get_available_vpns(self, type : _vpn_types):
        return self.request(RouteList.get_available_vpns(options={"type": type}))
    def get_vpn_info(self):
        return self.request(RouteList.get_vpn_info())
    
    # * VM

    def get_machine_running(self):
        return self.request(RouteList.get_machine_running())
    def post_renew_machine(self, room_code):
        return self.request(RouteList.post_renew_machine(), json={"code": room_code, "_csrf": ""})
    def post_terminate_machine(self, room_code):
        return self.request(RouteList.post_terminate_machine(), json={"code": room_code, "_csrf": ""})
    
    # * user -badge
    
    def get_own_badges(self):
        return self.request(RouteList.get_own_badges())
    def get_user_badges(self, username):
        return self.request(RouteList.get_user_badges(username=username))
    def get_all_badges(self):
        return self.request(RouteList.get_all_badges())
    
    # * user -team
    
    def get_team_info(self): 
        return self.request(RouteList.get_team_info())
    
    # * user -notifications
    
    def get_unseen_notifications(self):
        return self.request(RouteList.get_unseen_notifications())
    def get_all_notifications(self):
        return self.request(RouteList.get_all_notifications())

    # * user -messages

    def get_unseen_messages(self):
        return self.request(RouteList.get_unseen_messages())
    def get_all_group_messages(self):
        return self.request(RouteList.get_all_group_messages())
    
    # * user -room

    def get_user_completed_rooms_count(self, username):
        return self.request(RouteList.get_user_completed_rooms_count(username=username))
    def get_user_completed_rooms(self, username, limit:int=10, page:int=1):
        return self.request(RouteList.get_user_completed_rooms(username=username, options={"limit": limit, "page": page}))
    def get_user_created_rooms(self, username, limit:int=10, page:int=1):
        return self.request(RouteList.get_user_created_rooms(username=username, options={"limit": limit, "page": page}))

    # * user

    def get_user_rank(self, username):
        return self.request(RouteList.get_user_rank(username=username))
    def get_user_activty(self, username):
        return self.request(RouteList.get_user_activty(username=username))
    def get_all_friends(self):
        return self.request(RouteList.get_all_friends())
    def get_discord_user(self, username):
        return self.request(RouteList.get_discord_user(username=username))
    def get_user_exist(self, username):
        return self.request(RouteList.get_user_exist(username=username))
    def search_user(self, username):
        return self.request(RouteList.search_user(username=username))

    # * room

    def get_new_rooms(self):
        return self.request(RouteList.get_new_rooms())
    def get_recommended_rooms(self):
        return self.request(RouteList.get_recommended_rooms())
    def get_questions_answered(self):
        return self.request(RouteList.get_questions_answered())
    def get_joined_rooms(self):
        return self.request(RouteList.get_joined_rooms())
    def get_room_percetages(self, room_codes):
        return self.request(RouteList.get_room_percetages(), json={"rooms": room_codes})
    def get_room_scoreboard(self, room_code):
        return self.request(RouteList.get_room_scoreboard(room_code=room_code))
    def get_room_votes(self, room_code):
        return self.request(RouteList.get_room_votes(room_code=room_code))
    def get_room_details(self, room_code):
        return self.request(RouteList.get_room_details(room_code=room_code))
    def get_room_tasks(self, room_code):
        return self.request(RouteList.get_room_tasks(room_code=room_code))
    def post_room_answer(self, room_code, taskNo: int, questionNo: int, answer: str):
        return self.request(RouteList.post_room_answer(room_code=room_code), json={"_csrf": "", "taskNo": taskNo, "questionNo": questionNo, "answer": answer})
    def post_deploy_machine(self, room_code, uploadId): # ? csrf token
        return self.request(RouteList.post_deploy_machine(), json={"roomCode": room_code, "id": uploadId, "_csrf": ""})
    def post_reset_room_progress(self, room_code): # ? csrf token
        return self.request(RouteList.post_reset_room_progress(), json={"code": room_code, "_csrf": ""})
    def post_leave_room(self, room_code): # ? csrf token
        return self.request(RouteList.post_leave_room(), json={"code": room_code, "_csrf": ""})
    