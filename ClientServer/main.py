from ClientServer.config import url_top_news
from ClientServer.getData import News


def get_news_data():
    news_headlines = News(url_top_news)
    news_json_data = news_headlines.get_news_json()

    news_data = {}
    for i in range(5):
        headline = news_json_data['articles'][i]['title']
        content = news_json_data['articles'][i]['description']
        news_data[headline] = content

    return news_data


