import requests

from datetime import datetime
import pytz
import humanize

import config


def get_news_articles():
    try:
        url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={config.NEWS_API_KEY}"

        response = requests.get(url)

        response_json = response.json()

        date_format = '%Y-%m-%dT%H:%M:%SZ'
        news_articles = []

        if response_json.get('status') == 'ok' and response_json.get('totalResults') > 0:
            for article in response_json.get('articles'):
                source = article.get('source').get('name')
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')
                image_url = article.get('urlToImage')
                published_at = article.get('publishedAt')
                published_dt = datetime.strptime(published_at, date_format).replace(tzinfo=pytz.utc)

                current_time = datetime.now(pytz.utc)

                published_when = humanize.naturaltime(current_time - published_dt)

                news_article = {
                    'source': source,
                    'title': title,
                    'description': description,
                    'url': url,
                    'image_url': image_url,
                    'published_when': published_when
                }

                news_articles.append(news_article)

        return news_articles

    except Exception:
        return None
