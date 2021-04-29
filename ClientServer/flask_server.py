from flask import Flask

from ClientServer.main import get_news_data

app = Flask(__name__)


@app.route('/')
def home_page():
    return str(get_news_data())


@app.route('/headline')
def headlines():
    headline = get_news_data().keys()
    return str(headline)


if __name__ == "__main__":
    app.run()
