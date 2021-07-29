from .base_parser import BaseParser
from hltv.util import get_code_from_link

from selenium.webdriver.common.by import By


BASE_EVENT_URL = 'https://www.hltv.org/events/{}/test'


class EventParser(BaseParser):

    def __init__(self, event_code):
        super().__init__()
        self.event_code = event_code

    def __del__(self):
        self.driver.quit()

    def get_event_data(self):
        self.driver.get(BASE_EVENT_URL.format(self.event_code))

        if not self.is_site_load((By.CLASS_NAME, 'event-page')):
            return None

        event_link = self.driver.find_element_by_xpath("//a[@class='event-hub-top']")

        event_link_href = event_link.get_attribute('href')
        event_link_text = event_link.get_attribute('textContent').strip()

        return event_link_text, event_link_href

    def get_event_players(self):
        self.driver.get(BASE_EVENT_URL.format(self.event_code))

        if not self.is_site_load((By.CLASS_NAME, 'event-page')):
            return None

        players = self.driver.find_elements_by_xpath("//div[@class='flag-align player']//a")

        for player in players:
            player_text = player.get_attribute('textContent')
            player_href = player.get_attribute('href')
            player_code = get_code_from_link(player_href)

            yield player_code, player_href, player_text

    def get_event_mvp(self):
        self.driver.get('https://www.hltv.org/events/5469/test')

        if not self.is_site_load((By.CLASS_NAME, 'event-page')):
            return None

        player_mvp = self.driver.find_element_by_xpath("//div[@class='player-name']//a")

        player_mvp_text = player_mvp.get_attribute('textContent')
        player_mvp_href = player_mvp.get_attribute('href')
        player_mvp_code = get_code_from_link(player_mvp_text)

        return player_mvp_code, player_mvp_href, player_mvp_text
