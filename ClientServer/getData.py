import requests


class News:
    def __init__(self, news_url):
        self.url = news_url

    def _get_news_data(self):
        response = requests.get(url=self.url)
        return response.json()

    def get_news_json(self):
        return self._get_news_data()

