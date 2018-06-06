import requests
import requests_cache
from fake_useragent import UserAgent

requests_cache.install_cache('demo_cache')

FAKE_USER_AGENT = UserAgent()
HEADERS = {'content-encoding': 'gzip', 'User-Agent': FAKE_USER_AGENT.google}

def get_page(url):
    page = requests.get(url, headers=HEADERS)
    return page.text
