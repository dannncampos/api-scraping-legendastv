"""Service do Scraping do Legendas TV"""
from src.application.utils.tools import get_session
from src.crawlers.legendastv.business.business_legendas_tv import BusinessLegendasTv


class ServiceLegendasTv:
    """Legendas Tv class"""

    def __init__(self, term, user, password):
        """
        This is the constructor of Legendas Tv API

        Arguments:
            term {string} -- term for search
            user (str): Legendas Tv User's Login
            password (str): Legendas Tv User's Password
        """

        # Query attributes
        self.term = term
        self.user = user
        self.password = password

        # Session
        self.session = get_session()

        # URL Paths -> Get it from a config YML's file in the future
        self.host = 'legendas.tv'
        self.url_home_page = 'http://legendas.tv/'
        self.url_login = 'http://legendas.tv/login'
        self.url_do_search = 'http://legendas.tv/legenda/busca/'
        self.url_download = 'http://legendas.tv/downloadarquivo/'


    def capture_by_term(self):
        """ It calls the method to capture by term"""
        return BusinessLegendasTv.capture_by_term(self)
