import os


class Config:

    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,bloomberg,engadget,espn,fortune,al-jazeera-english,cnn,independent&pageSize={}&apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize={}&apiKey={}'
    EVERYTHING_SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&pageSize={}&apiKey={}'
    KENYA_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&country=ke&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    """
    ProdConfig= DevConfig I am your father
    DevConfig = No!!!!
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
