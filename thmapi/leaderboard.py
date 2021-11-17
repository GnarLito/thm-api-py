from .util import *


class __THMLeaderboard(object):
    def get_leaderboard(self, monthly=True, country=None) -> list:
        """
        Returns the top 50 users from the all-time leaderboard

        :param monthly Switch for the monthly data
        :type monthly: bool
        :param country: Country code for country leaderboards
        :type country: str
        :return: List containing top 50 users
        """

        queries = []
        if monthly:
            queries.append('type=monthly')

        if country:
            queries.append(f'country={country}')

        query = '?' + '&'.join(queries)

        return http_get(self.session, '/api/leaderboards' + query)['ranks']

    def get_koth_leaderboard(self, monthly=True, country=None) -> list:
        """
        Returns the top 50 users from the all-time king of the hill leaderboard

        :param monthly Switch for the monthly data
        :type monthly: bool
        :param country: Country code for country king of the hill leaderboards
        :type country: str
        :return: List containing top 50 users
        """

        queries = []
        if monthly:
            queries.append('type=monthly')

        if country:
            queries.append(f'country={country}')

        query = '?' + '&'.join(queries)

        return http_get(self.session, '/api/leaderboards/koth' + query)['ranks']
