from .auth import __THMAuth
from .instance import __THMInstance
from .koth import __THMKoth
from .leaderboard import __THMLeaderboard
from .room import __THMRoom

from .user import __THMUser
import requests


class THM(
    __THMAuth,
    __THMLeaderboard,
    __THMUser,
    __THMKoth,
    __THMRoom,
    __THMInstance
):
    """
    TryHackMe API Wrapper
    """

    def __init__(self, credentials=None):
        """
        Initializes the API Wrapper

        :type credentials: dict
        :param credentials: (Optional) Credentials for use with authenticated requests
        """

        self.session = requests.Session()
        self.authenticated = False

        if (credentials is not None) and (type(credentials) == dict):
            if ('username' in credentials) and ('password' in credentials) or 'session' in credentials:
                self.login(credentials)



__version__ = "1.0"