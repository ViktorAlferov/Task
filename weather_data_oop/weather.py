# module with weathers
from urllib.parse import urlparse

class Weather():
    def __init__(self, url=None):
        self.url = url

    @property
    def domain(self):
        domain = urlparse(self.url)
        return domain.netloc





