"""Business do Scraping Legendas TV"""
from src.crawlers.legendastv.broker import broker_legendastv as broker
from src.crawlers.legendastv.parser import parser_legendastv as parser


class BusinessLegendasTv:
    """Classe de Business para Scraping Legendas TV"""

    def capture_by_term(self):

        # First Response
        first_reponse = broker.get_first_response(self.url_home_page, self.host, self.session)

        login_page = broker.do_login(self.url_login, self.host, self.url_home_page, self.user, self.password, self.session)

        result_page = broker.search_term(self.url_do_search, self.host, self.url_home_page, self.term, self.session)

        page_number = 1

        results = []
        for x in parser.extract_subtitle_info(result_page.text, self.url_download): results.append(x)

        while (parser.has_more_pages(result_page.text)):
            result_page = broker.get_next_pages(self.url_do_search, self.host, self.term, self.session, page_number)
            for x in parser.extract_subtitle_info(result_page.text, self.url_download): results.append(x)
            page_number += 1
        
        return results
